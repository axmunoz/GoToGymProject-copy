from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from products.models import Product

# Añadir producto al carrito
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        cart_count = sum(cart.values())
        return JsonResponse({'success': True, 'cart_count': cart_count})
    return redirect('carrito:cart_detail')

# Eliminar producto del carrito
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('carrito:cart_detail')

# Actualizar cantidad
def update_cart(request, product_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        cantidad_actual = cart.get(str(product_id), 1)
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
            cart[str(product_id)] = cantidad_actual
        else:
            cart.pop(str(product_id), None)
        request.session['cart'] = cart
    return redirect('carrito:cart_detail')

# Mostrar carrito
def cart_detail(request):
    cart = request.session.get('cart', {})
    productos = Product.objects.filter(id__in=cart.keys())
    items = []
    total = 0
    total_original = 0
    from decimal import Decimal, ROUND_HALF_UP
    ahorro_total = Decimal('0.00')
    total_original = Decimal('0.00')
    for producto in productos:
        cantidad = cart[str(producto.id)]
        subtotal = (producto.discounted_price * cantidad).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        subtotal_original = (producto.price * cantidad).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        descuento_producto = (producto.price * (Decimal(producto.discount) / Decimal('100')) * cantidad).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        items.append({'producto': producto, 'cantidad': cantidad, 'subtotal': subtotal, 'subtotal_original': subtotal_original})
        total += subtotal
        total_original += subtotal_original
        ahorro_total += descuento_producto
    total = Decimal(total).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    total_original = total_original.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    ahorro_total = ahorro_total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    shipping = 5 if items else 0
    total_price = total + shipping

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
    # Usar la variable correcta de settings
    mp_public_key = getattr(settings, 'MP_PUBLIC_KEY', '')
    total_sin_envio = (total_original - ahorro_total).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return render(request, 'carrito/cart_detail.html', {
        'items': items,
        'total': total,
        'total_original': total_original,
        'shipping': shipping,
        'total_price': total_price,
        'num_items': sum(cart.values()),
        'mp_public_key': mp_public_key,
        'ahorro_total': ahorro_total,
        'total_sin_envio': total_sin_envio,
    })
