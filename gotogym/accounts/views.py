from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.contrib import messages
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.utils import timezone
from pathlib import Path
import hashlib
from .models import User
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
from carrito.models import CarritoHistorial, CarritoHistorialItem

from .forms import EditProfileForm

TERMS_PATH = Path(__file__).resolve().parent / 'templates' / 'accounts' / 'terms_and_conditions.html'

User = get_user_model()

def logout_view(request):
    logout(request)
    return redirect('/')

@csrf_protect
def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        # Autocompletar username con la parte antes del @
        username = email.split('@')[0] if email else ''
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        accepted_terms = request.POST.get('accepted_terms')
        # Validaciones básicas
        if not all([first_name, last_name, age, email, password1, password2, accepted_terms]):
            messages.error(request, 'Todos los campos son obligatorios.')
        elif password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'El correo ya está registrado.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está registrado.')
        else:
            terms_text = TERMS_PATH.read_text(encoding='utf-8')
            user = User.objects.create_user(
                email=email,
                username=username,
                first_name=first_name,
                last_name=last_name,
                age=age,
                password=password1,
                accepted_terms=True,
                terms_accepted_at=timezone.now(),
                terms_hash=hashlib.sha512(terms_text.encode()).hexdigest(),
            )
            # Crear contacto en HubSpot automáticamente
            try:
                from hubspot_integration.hubspot_utils import create_hubspot_contact
                create_hubspot_contact(email, first_name, last_name)
            except Exception as e:
                messages.warning(request, f'Usuario creado, pero no se pudo crear el contacto en HubSpot: {e}')
            messages.success(request, f'Registro exitoso. Tu usuario es: {username}. Ahora puedes iniciar sesión.')
            return redirect('login')
    return render(request, 'accounts/register.html')

@csrf_protect
def login_view(request):
    show_logo = request.session.pop('show_logo', True)
    error_message = None
    if request.method == 'POST':
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')
        # Buscar usuario por username o email
        try:
            user_obj = User.objects.get(username=username_or_email)
        except User.DoesNotExist:
            try:
                user_obj = User.objects.get(email=username_or_email)
            except User.DoesNotExist:
                user_obj = None
        user = None
        if user_obj:
            user = authenticate(request, username=user_obj.email, password=password)
            if user is not None:
                # Si es admin y le falta nombre o apellido, redirigir a editar perfil
                if user.is_superuser and (not user.first_name or not user.last_name or user.first_name == 'None' or user.last_name == 'None'):
                    login(request, user)
                    return redirect(reverse('edit_profile'))
                login(request, user)
                # Sincronizar carrito de sesión con historial pendiente
                try:
                    carrito_historial = CarritoHistorial.objects.get(usuario=user, estado='pendiente')
                    cart_session = {}
                    for item in carrito_historial.items.all():
                        key = f"{item.product.id}:{item.talla if item.talla else ''}"
                        cart_session[key] = item.cantidad
                    request.session['cart'] = cart_session
                    # Restaurar cupón y total_pagar si existen
                    if carrito_historial.cupon_code:
                        # Recalcular descuento para mostrar en sesión
                        total_sin_descuento = sum(
                            (item.product.price * item.cantidad)
                            for item in carrito_historial.items.all()
                        )
                        envio = 20000 if cart_session else 0
                        base_cupon = total_sin_descuento + envio
                        discount_value = int(base_cupon * 0.10)
                        request.session['coupon'] = discount_value
                        request.session['coupon_code'] = carrito_historial.cupon_code
                        request.session['coupon_percent'] = 10
                    else:
                        request.session['coupon'] = 0
                        request.session['coupon_code'] = ''
                        request.session['coupon_percent'] = 0
                except CarritoHistorial.DoesNotExist:
                    request.session['cart'] = {}
                    request.session['coupon'] = 0
                    request.session['coupon_code'] = ''
                    request.session['coupon_percent'] = 0
                next_url = request.POST.get('next') or request.GET.get('next')
                if next_url and '/carrito' in next_url:
                    return redirect(next_url)
                return redirect('/')
        else:
            error_message = _('Credenciales incorrectas')
    return render(request, 'accounts/login.html', {'error_message': error_message, 'show_logo': show_logo})

@login_required
def profile_view(request):
    carritos_pagados = CarritoHistorial.objects.filter(usuario=request.user, estado='pagado').order_by('-fecha_actualizacion')
    return render(request, 'accounts/profile.html', {
        'user': request.user,
        'base_template': '_base_dasboard.html' if request.user.is_superuser else 'base.html',
        'carritos_pagados': carritos_pagados,
    })

# View to edit user profile
@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        print('FILES ENVIADOS:', request.FILES)
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            # Actualizar campos del usuario
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.phone_number = form.cleaned_data['phone_number']
            user.age = form.cleaned_data['age']
            user.weight = form.cleaned_data['weight']
            user.city = form.cleaned_data['city']
            user.height = form.cleaned_data['height']
            # Eliminar imagen anterior si se sube una nueva
            if 'image' in request.FILES:
                if user.image:
                    user.image.delete(save=False)
                user.image = request.FILES['image']
            user.save()
            print('IMAGEN GUARDADA:', user.image)
            
            return redirect('profile')
        else:
            print('ERRORES FORMULARIO:', form.errors)
            messages.error(request, _('Por favor corrige los errores en el formulario.'))
    else:
        form = EditProfileForm(instance=user)
    return render(request, 'accounts/edit_profile.html', {
        'form': form,
        'user': user,
        'base_template': '_base_dasboard.html' if user.is_superuser else 'base.html',
    })
