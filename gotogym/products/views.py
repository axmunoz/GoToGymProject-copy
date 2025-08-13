from .models import Talla
from django.shortcuts import render, redirect, get_object_or_404
from .models import ProductCategory, Product, Brand, ProductImage, ProductVideo
from django import forms
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .forms import ProductForm

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'description']

def add_category(request):
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            from django.contrib import messages
            messages.success(request, 'Categoría añadida con éxito')
            return redirect('products:list_category')
    else:
        form = ProductCategoryForm()
    return render(request, 'products/add_category.html', {'form': form})

def add_product(request):
    from .forms import ProductForm, ProductImageForm, ProductVideoForm
    marcas = Brand.objects.all().order_by('name')
    categorias = ProductCategory.objects.all().order_by('name')
    tallas = Talla.objects.all().order_by('nombre')
    if request.method == 'POST':
        # Sumar el stock total de los campos ocultos antes de crear el formulario
        post_data = request.POST.copy()
        try:
            stock_total = int(post_data.get('stock_total', 0))
        except (ValueError, TypeError):
            stock_total = 0
        post_data['stock'] = stock_total
        form = ProductForm(post_data, request.FILES)
        video_form = ProductVideoForm(request.POST, request.FILES)
        valid = form.is_valid()
        valid_video = True
        # Si hay video, validar el form de video
        if 'video' in request.FILES:
            valid_video = video_form.is_valid()
        if valid and valid_video:
            product = form.save()
            # Imágenes
            images = request.FILES.getlist('images')
            for idx, img in enumerate(images):
                if idx < 7:
                    ProductImage.objects.create(product=product, image=img)
            # Video
            if 'video' in request.FILES:
                ProductVideo.objects.create(product=product, video=request.FILES['video'])

            # Guardar stock por tallas personalizadas
            from .models import ProductStock
            import json
            stock_tallas_json = request.POST.get('stock_tallas', '')
            if stock_tallas_json:
                try:
                    tallas_data = json.loads(stock_tallas_json)
                except Exception:
                    tallas_data = []
                for item in tallas_data:
                    talla = item.get('talla', '').strip()
                    try:
                        cantidad = int(item.get('cantidad', 0))
                    except (ValueError, TypeError):
                        cantidad = 0
                    if talla and cantidad > 0:
                        ProductStock.objects.create(product=product, talla=talla, cantidad=cantidad)

            return redirect('products:list_product')
        # Si no es válido, mostrar errores
    else:
        form = ProductForm()
        video_form = ProductVideoForm()
    image_form = ProductImageForm()
    return render(request, 'products/add_product.html', {
        'form': form,
        'image_form': image_form,
        'video_form': video_form,
        'marcas': marcas,
        'categorias': categorias,
        'tallas': tallas
    })

# Endpoint para crear tallas desde el modal (AJAX)
@csrf_exempt
@require_POST
def crear_tallas(request):
    import json
    data = json.loads(request.body.decode('utf-8'))
    nombres = data.get('tallas', [])
    creadas = []
    for nombre in nombres:
        nombre = nombre.strip()
        if nombre:
            obj, created = Talla.objects.get_or_create(nombre=nombre)
            if created:
                creadas.append(obj.nombre)
    return JsonResponse({'ok': True, 'creadas': creadas})

def list_category(request):
    categories = ProductCategory.objects.all()
    paginator = Paginator(categories, 4)  # 4 categorías por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products/list_category.html', {'categories': page_obj, 'page_obj': page_obj})

def list_product(request):
    products = Product.objects.select_related('category').all()
    paginator = Paginator(products, 4)  # 4 productos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products/list_product.html', {'products': page_obj, 'page_obj': page_obj})

def view_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/view_product.html', {'product': product})

def edit_product(request, pk):
    from .forms import ProductForm, ProductImageForm, ProductVideoForm
    product = get_object_or_404(Product, pk=pk)
    marcas = Brand.objects.all().order_by('name')
    categorias = ProductCategory.objects.all().order_by('name')
    max_images_left = 7 - product.images.count()
    if request.method == 'POST':
        post_data = request.POST.copy()
        try:
            stock_total = int(post_data.get('stock_total', 0))
        except (ValueError, TypeError):
            stock_total = 0
        post_data['stock'] = stock_total
        form = ProductForm(post_data, request.FILES, instance=product)
        image_form = ProductImageForm(request.POST, request.FILES)
        video_form = ProductVideoForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            from .models import ProductStock
            import json
            stock_tallas_json = post_data.get('stock_tallas', '')
            ProductStock.objects.filter(product=product).delete()
            total_stock = 0
            if stock_tallas_json:
                try:
                    tallas_data = json.loads(stock_tallas_json)
                except Exception:
                    tallas_data = []
                for item in tallas_data:
                    talla = item.get('talla', '').strip()
                    try:
                        cantidad = int(item.get('cantidad', item.get('stock', 0)))
                    except (ValueError, TypeError):
                        cantidad = 0
                    if talla and cantidad > 0:
                        ProductStock.objects.create(product=product, talla=talla, cantidad=cantidad)
                        total_stock += cantidad
            # Actualizar el stock total en el producto
            product.stock = total_stock
            product.save(update_fields=['stock'])
            # Eliminar imágenes marcadas para borrar
            deleted_images = request.POST.get('deleted_images', '')
            if deleted_images:
                ids = [int(i) for i in deleted_images.split(',') if i.isdigit()]
                for img_id in ids:
                    try:
                        img = ProductImage.objects.get(id=img_id, product=product)
                        img.delete()
                    except ProductImage.DoesNotExist:
                        pass
            # Imágenes nuevas
            images = request.FILES.getlist('image')
            for idx, img in enumerate(images):
                if idx < 7:
                    ProductImage.objects.create(product=product, image=img)
            # Video nuevo
            if 'video' in request.FILES:
                # Si ya existe, reemplaza
                if hasattr(product, 'video'):
                    product.video.video.delete(save=False)
                    product.video.delete()
                ProductVideo.objects.create(product=product, video=request.FILES['video'])
            return redirect('products:list_product')
    else:
        form = ProductForm(instance=product)
        image_form = ProductImageForm()
        video_form = ProductVideoForm()
    # Generar JSON de stock por talla para el JS
    from .models import ProductStock
    import json
    stock_qs = ProductStock.objects.filter(product=product)
    stock_tallas_list = [
        {'talla': s.talla, 'stock': s.cantidad} for s in stock_qs
    ]
    stock_tallas_json = json.dumps(stock_tallas_list)
    tallas_qs = Talla.objects.all().order_by('nombre')
    tallas = list(tallas_qs.values('id', 'nombre'))
    return render(request, 'products/edit_product.html', {
        'form': form,
        'image_form': image_form,
        'video_form': video_form,
        'edit': True,
        'product': product,
        'marcas': marcas,
        'categorias': categorias,
        'max_images_left': max_images_left,
        'stock_tallas_json': stock_tallas_json,
        'tallas': tallas
    })

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products:list_product')
    return render(request, 'products/delete_product.html', {'product': product})

@csrf_exempt
def delete_product_image(request, pk):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=pk)
        if product.image:
            product.image.delete(save=False)
            product.image = None
            product.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)


def delete_product_video(request, pk):
    if request.method == 'POST':
        from .models import ProductVideo
        product = get_object_or_404(Product, pk=pk)
        try:
            product_video = ProductVideo.objects.get(product=product)
            if product_video.video:
                product_video.video.delete(save=False)
            product_video.delete()
            return JsonResponse({'success': True})
        except ProductVideo.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'No video found'}, status=404)
    return JsonResponse({'success': False}, status=400)

def edit_category(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            from django.contrib import messages
            messages.success(request, 'Categoría actualizada correctamente')
            return redirect('products:list_category')
    else:
        form = ProductCategoryForm(instance=category)
    return render(request, 'products/edit_category.html', {'form': form, 'category': category})

def delete_category(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('products:list_category')
    return render(request, 'products/delete_category.html', {'category': category})

@csrf_exempt
def delete_category_ajax(request, pk):
    if request.method == 'POST':
        category = get_object_or_404(ProductCategory, pk=pk)
        category.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

def view_category(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    return render(request, 'products/view_category.html', {'category': category})

# Listar y añadir marca
def brand_list(request):
    marcas = Brand.objects.all().order_by('name')
    marca = None
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Brand.objects.create(name=name)
            return redirect('products:brand_list')
    return render(request, 'products/brand_list.html', {'marcas': marcas, 'marca': marca})

# Editar marca
def brand_edit(request, pk):
    marca = get_object_or_404(Brand, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
        import sys
        print(f"[DEBUG] Valor recibido para name: {name}", file=sys.stderr)
        saved = False
        if name:
            marca.name = name
            marca.save()
            saved = True
            print(f"[DEBUG] Marca guardada: id={marca.id}, name={marca.name}", file=sys.stderr)
            if is_ajax:
                return JsonResponse({
                    'id': marca.id,
                    'name': marca.name,
                    'received': name,
                    'saved': saved,
                    'method': request.method
                })
            return redirect('products:brand_list')
        if is_ajax:
            return JsonResponse({
                'error': 'No name provided',
                'received': name,
                'saved': saved,
                'method': request.method
            }, status=400)
        return redirect('products:brand_list')
    marcas = Brand.objects.all().order_by('name')
    return render(request, 'products/brand_list.html', {'marcas': marcas, 'marca': marca})

# Previsualizar marca
def brand_preview(request, pk):
    marca = get_object_or_404(Brand, pk=pk)
    return render(request, 'products/brand_preview.html', {'marca': marca})

# Eliminar marca
@require_POST
def brand_delete(request, pk):
    marca = get_object_or_404(Brand, pk=pk)
    marca.delete()
    return redirect('products:brand_list')
