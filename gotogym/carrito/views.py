from influencer.models import InfluencerProfile
# Vista para aplicar cupón de influencer
from django.views.decorators.http import require_POST
@require_POST
def apply_coupon(request):
    code = request.POST.get('coupon_code', '').strip().upper()
    # Guardar el cupón en el historial del carrito si el usuario está autenticado
    cart = request.session.get('cart', {})
    if request.user.is_authenticated:
        from .models import CarritoHistorial
        carrito = CarritoHistorial.objects.filter(usuario=request.user, estado='pendiente').first()
        if carrito:
            carrito.cupon_code = code
            # Calcular el total a pagar igual que en la vista principal
            total_sin_descuento = 0
            for key, cantidad in cart.items():
                parts = key.split(":")
                product_id = parts[0]
                producto = Product.objects.filter(id=product_id).first()
                if producto:
                    total_sin_descuento += float(producto.price) * cantidad
            envio = 20000 if cart else 0
            base_cupon = total_sin_descuento + envio
            discount_value = int(base_cupon * 0.10)
            total_pagar = base_cupon - discount_value
            carrito.total_pagar = int(total_pagar)
            carrito.save()
    influencer = InfluencerProfile.objects.filter(coupon_code=code, is_active=True).first()
    if influencer:
        # Aplica el cupón sobre el total sin descuento + envío
        cart = request.session.get('cart', {})
        total_sin_descuento = 0
        for key, cantidad in cart.items():
            parts = key.split(":")
            product_id = parts[0]
            producto = Product.objects.filter(id=product_id).first()
            if producto:
                total_sin_descuento += float(producto.price) * cantidad
        envio = 20000 if cart else 0
        base_cupon = total_sin_descuento + envio
        discount_value = int(base_cupon * 0.10)
        request.session['coupon'] = discount_value
        request.session['coupon_code'] = code
        request.session['coupon_percent'] = 10
        
    else:
        request.session['coupon'] = 0
        request.session['coupon_code'] = ''
        messages.error(request, 'Cupón inválido o inactivo.')
    return redirect('carrito:cart_detail')
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from products.models import Product


# Añadir producto al carrito
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    talla = request.POST.get('talla') or request.GET.get('talla') or ''
    key = f"{product_id}:{talla}"
    cart[key] = cart.get(key, 0) + 1
    request.session['cart'] = cart

    # Guardar en la base de datos
    from .models import CarritoHistorial, CarritoHistorialItem
    if request.user.is_authenticated:
        carrito, created = CarritoHistorial.objects.get_or_create(
            usuario=request.user,
            estado='pendiente'
        )
        # Buscar si ya existe el item con ese producto y talla
        item, item_created = CarritoHistorialItem.objects.get_or_create(
            carrito=carrito,
            product_id=product_id,
            talla=talla
        )
        if not item_created:
            item.cantidad += 1
            item.save()
        # Calcular y actualizar total_pagar después de añadir el producto
        from decimal import Decimal
        items = list(carrito.items.all())
        total = sum(i.product.price * Decimal(i.cantidad) for i in items)
        total_discount = sum(
            (i.product.price - i.product.discounted_price) * Decimal(i.cantidad)
            if i.product.discount > 0 else Decimal('0')
            for i in items
        )
        total_before_shipping = total - total_discount
        shipping = Decimal('20000') if items else Decimal('0')
        coupon_value = Decimal(str(request.session.get('coupon', 0)))
        total_pagar = total_before_shipping + shipping - coupon_value
        carrito.total_pagar = int(total_pagar)
        carrito.save()
    # Si no está autenticado, solo guarda en sesión

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        cart_count = sum(cart.values())
        return JsonResponse({'success': True, 'cart_count': cart_count})
    return redirect('carrito:cart_detail')

# Eliminar producto del carrito
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    talla = request.GET.get('talla') or request.POST.get('talla') or ''
    key = f"{product_id}:{talla}"
    if key in cart:
        del cart[key]
        request.session['cart'] = cart
        # Eliminar en la base de datos
        from .models import CarritoHistorial, CarritoHistorialItem
        if request.user.is_authenticated:
            carrito = CarritoHistorial.objects.filter(usuario=request.user, estado='pendiente').first()
            if carrito:
                item = CarritoHistorialItem.objects.filter(carrito=carrito, product_id=product_id, talla=talla).first()
                if item:
                    item.delete()
                # Si ya no quedan items, eliminar el carrito y el cupón
                if not carrito.items.exists():
                    # Eliminar cupón de la sesión
                    request.session['coupon'] = 0
                    request.session['coupon_code'] = ''
                    request.session['coupon_percent'] = 0
                    # Eliminar cupón de la base de datos
                    carrito.cupon_code = ''
                    carrito.total_pagar = 0
                    carrito.save()
                    carrito.delete()
    return redirect('carrito:cart_detail')

def remove_coupon(request):
    # Eliminar cupón de la sesión
    request.session['coupon'] = 0
    request.session['coupon_code'] = ''
    request.session['coupon_percent'] = 0
    # Eliminar cupón de la base de datos
    if request.user.is_authenticated:
        from .models import CarritoHistorial
        carrito = CarritoHistorial.objects.filter(usuario=request.user, estado='pendiente').first()
        if carrito:
            carrito.cupon_code = ''
            # Recalcular total_pagar sin cupón
            from decimal import Decimal
            items = list(carrito.items.all())
            total = sum(i.product.price * Decimal(i.cantidad) for i in items)
            total_discount = sum(
                (i.product.price - i.product.discounted_price) * Decimal(i.cantidad)
                if i.product.discount > 0 else Decimal('0')
                for i in items
            )
            total_before_shipping = total - total_discount
            shipping = Decimal('20000') if items else Decimal('0')
            total_pagar = total_before_shipping + shipping
            carrito.total_pagar = int(total_pagar)
            carrito.save()
    
    return redirect('carrito:cart_detail')
# Actualizar cantidad
def update_cart(request, product_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        talla = request.POST.get('talla') or ''
        key = f"{product_id}:{talla}"
        cantidad_actual = cart.get(key, 1)
        accion = request.POST.get('accion')
        cantidad_input = request.POST.get('cantidad')
        if accion == 'sumar':
            cantidad_actual += 1
        elif accion == 'restar':
            cantidad_actual -= 1
        elif cantidad_input:
            try:
                cantidad_actual = int(cantidad_input)
            except ValueError:
                cantidad_actual = 1
        if cantidad_actual > 0:
            cart[key] = cantidad_actual
        else:
            cart.pop(key, None)
        request.session['cart'] = cart

        # Actualizar en la base de datos
        from .models import CarritoHistorialItem, CarritoHistorial
        if request.user.is_authenticated:
            carrito = CarritoHistorial.objects.filter(usuario=request.user, estado='pendiente').first()
            if carrito:
                item = CarritoHistorialItem.objects.filter(carrito=carrito, product_id=product_id, talla=talla).first()
                if item:
                    if cantidad_actual > 0:
                        item.cantidad = cantidad_actual
                        item.save()
                    else:
                        item.delete()
                # Actualizar total_pagar después de modificar el carrito
                cart_items = CarritoHistorialItem.objects.filter(carrito=carrito)
                from decimal import Decimal
                items = list(cart_items)
                total = sum(i.product.price * Decimal(i.cantidad) for i in items)
                total_discount = sum(
                    (i.product.price - i.product.discounted_price) * Decimal(i.cantidad)
                    if i.product.discount > 0 else Decimal('0')
                    for i in items
                )
                total_before_shipping = total - total_discount
                shipping = Decimal('20000') if items else Decimal('0')
                coupon_value = Decimal(str(request.session.get('coupon', 0)))
                total_pagar = total_before_shipping + shipping - coupon_value
                carrito.total_pagar = int(total_pagar)
                carrito.save()
                # Si el carrito está vacío, eliminar el cupón
                if not items:
                    request.session['coupon'] = 0
                    request.session['coupon_code'] = ''
                    request.session['coupon_percent'] = 0
                    carrito.cupon_code = ''
                    carrito.save()
    return redirect('carrito:cart_detail')

# Mostrar carrito
def cart_detail(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    grouped_items = {}
    # cart: key = "product_id:talla", value = cantidad
    for key, cantidad in cart.items():
        parts = key.split(":")
        product_id = parts[0]
        talla = parts[1] if len(parts) > 1 else ''
        producto = Product.objects.filter(id=product_id).first()
        if not producto:
            continue
        subtotal = producto.price * cantidad
        # Calcular total con descuento si aplica
        if producto.discount > 0:
            total_descuento = float(producto.discounted_price) * cantidad
        else:
            total_descuento = subtotal
        item = {
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal,
            'talla': talla,
            'total_descuento': total_descuento
        }
        items.append(item)
        total += subtotal
        # Agrupación por producto
        if producto.id not in grouped_items:
            grouped_items[producto.id] = {'grouper': producto, 'list': [], 'group_subtotal': 0}
        grouped_items[producto.id]['list'].append(item)
        grouped_items[producto.id]['group_subtotal'] += item['total_descuento']
    grouped_items_list = list(grouped_items.values())
    # Envío fijo de 20,000
    shipping = 20000 if items else 0

    # Calcular descuento total
    total_discount = 0
    total_descuento_items = 0
    for item in items:
        if item['producto'].discount > 0:
            total_discount += (item['producto'].price - item['producto'].discounted_price) * item['cantidad']
        total_descuento_items += item['total_descuento']

    # Total antes de envío (total menos descuento)
    total_before_shipping = total - total_discount

    # Cupón
    coupon_value = request.session.get('coupon', 0)

    # Total a pagar
    total_pagar = total_before_shipping + shipping - int(coupon_value)

    # Mostrar estado de pago de MercadoPago si viene en la URL
    payment_status = request.GET.get('collection_status')
    if payment_status == 'approved':
        messages.success(request, '¡Pago aprobado! Gracias por tu compra.')
        # Limpiar carrito si el pago fue exitoso
        request.session['cart'] = {}
    elif payment_status == 'pending':
        messages.info(request, 'El pago está pendiente. Te notificaremos cuando se acredite.')
    elif payment_status == 'rejected':
        messages.error(request, 'El pago fue rechazado. Intenta nuevamente.')

    from django.conf import settings
    return render(request, 'carrito/cart_detail.html', {
        'items': items,
        'grouped_items': grouped_items_list,
        'total': total,
        'shipping': shipping,
    # 'total_price': total_price,  # Eliminado, ahora se usa total_pagar
        'total_pagar': int(total_pagar),
        'num_items': sum(cart.values()),
        'mp_public_key': getattr(settings, 'MERCADOPAGO_PUBLIC_KEY', ''),
        'total_discount': int(total_discount),
        'total_before_shipping': int(total_before_shipping),
        'coupon_value': int(coupon_value),
    })

# Vista para mostrar el resumen de compra
def resumen_compra(request, historial_id):
    # Aquí deberías obtener el historial de compra según el modelo que uses
    # Ejemplo básico:
    # historial = get_object_or_404(HistorialCompra, id=historial_id)
    # return render(request, 'carrito/resumen_compra.html', {'historial': historial})
    # Si no tienes el modelo, muestra una página básica:
    return render(request, 'carrito/resumen_compra.html', {'historial_id': historial_id})

# Vista para mostrar el historial de compras
def historial_compras(request):
    # Aquí deberías obtener la lista de compras del usuario según el modelo que uses
    # Ejemplo básico:
    # compras = HistorialCompra.objects.filter(usuario=request.user)
    # return render(request, 'carrito/historial_compras.html', {'compras': compras})
    # Si no tienes el modelo, muestra una página básica:
    return render(request, 'carrito/historial_compras.html')
