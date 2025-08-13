from django.shortcuts import render, get_object_or_404
from products.models import Product, ProductCategory, Brand
from django.core.paginator import Paginator
from django.db.models import F
from influencer.models import InfluencerProfile

def producto_list(request):
    productos = Product.objects.all().prefetch_related('images')
    categorias = ProductCategory.objects.all()
    marcas = Brand.objects.all()
    filtro = request.GET.get('filtro', '')
    categoria_id = request.GET.get('categoria')
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')
    rating = request.GET.get('rating')
    orden = request.GET.get('orden')

    if filtro:
        productos = productos.filter(name__icontains=filtro)
    if categoria_id:
        productos = productos.filter(category_id=categoria_id)
    if precio_min:
        productos = productos.filter(price__gte=precio_min)
    if precio_max:
        productos = productos.filter(price__lte=precio_max)
    if rating:
        try:
            rating_value = float(rating)
            productos = productos.filter(rating__gte=rating_value)
        except Exception:
            pass
    if orden == 'precio_asc':
        productos = productos.order_by('price')
    elif orden == 'precio_desc':
        productos = productos.order_by('-price')
    elif orden == 'nombre_asc':
        productos = productos.order_by('name')
    elif orden == 'nombre_desc':
        productos = productos.order_by('-name')

    # Forzar el cálculo del precio con descuento para cada producto
    productos_list = list(productos)
    for producto in productos_list:
        producto.save()  # Esto recalcula discounted_price si discount cambió

    paginator = Paginator(productos_list, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    featured_products = Product.objects.filter(featured=True).prefetch_related('images')

    context = {
        'productos': page_obj,
        'categorias': categorias,
        'marcas': marcas,
        'filtro': filtro,
        'page_obj': page_obj,
        'featured_products': featured_products,
    }
    return render(request, 'tienda/producto_list.html', context)

def producto_detail(request, pk):
    producto = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=producto.category).exclude(pk=producto.pk)[:4]
    influencer_profile = None
    if request.user.is_authenticated:
        influencer_profile = getattr(request.user, 'influencer_profile', None)
    # Obtener tallas disponibles para el producto
    tallas_disponibles = producto.stocks.filter(cantidad__gt=0).values_list('talla', flat=True)
    context = {
        'producto': producto,
        'related_products': related_products,
        'user': request.user,
        'influencer_profile': influencer_profile,
        'tallas_disponibles': tallas_disponibles,
    }
    return render(request, 'tienda/producto_detail.html', context)
