from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_POST
from .models import InfluencerProfile

# Solo superusuarios pueden acceder
def superuser_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

@superuser_required
def influencer_admin_list(request):
    influencers = InfluencerProfile.objects.select_related('user').all()
    return render(request, 'influencer/admin_list.html', {'influencers': influencers})

@superuser_required
@require_POST
def influencer_admin_delete(request, pk):
    influencer = InfluencerProfile.objects.filter(pk=pk).first()
    if influencer:
        influencer.delete()
    return redirect('influencer_admin_list')

@superuser_required
@require_POST
def influencer_admin_edit(request, pk):
    influencer = InfluencerProfile.objects.filter(pk=pk).first()
    if influencer:
        commission = request.POST.get('commission')
        try:
            commission = float(commission)
            influencer.commission_percent = commission
            influencer.save()
            # Recalcular comisión de compras pendientes
            from influencer.models import CompraReferida
            compras_pendientes = CompraReferida.objects.filter(influencer=influencer, estado='pendiente')
            for compra in compras_pendientes:
                compra.comision = compra.calcular_comision()
                compra.save()
        except Exception:
            pass
    # Redirige correctamente a la lista de influencers con anchor
    from django.urls import reverse
    url = reverse('influencer_admin_list') + f'#influencer-{pk}'
    return redirect(url)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models
from .models import InfluencerProfile
from django.db import IntegrityError


@login_required
def suscribete(request):
    user = request.user
    if hasattr(user, 'influencer_profile'):
        messages.info(request, 'Ya eres influencer.')
        return redirect('influencer_dashboard')
    try:
        InfluencerProfile.objects.create(user=user)
        messages.success(request, '¡Ahora eres influencer!')
    except IntegrityError:
        messages.error(request, 'Hubo un problema al suscribirte. Intenta de nuevo.')
    return redirect('influencer_dashboard')

@login_required
def dashboard(request):
    profile = getattr(request.user, 'influencer_profile', None)
    if not profile:
        return redirect('influencer_suscribete')
    from influencer.models import CompraReferida
    compras = CompraReferida.objects.filter(influencer=profile).order_by('-fecha')
    comision_pendiente = sum([c.comision for c in compras.filter(estado='pendiente')])
    comision_completada = sum([c.comision for c in compras.filter(estado='completada')])
    referidos_pendiente = compras.filter(estado='pendiente').count()
    referidos_completado = compras.filter(estado='completada').count()
    valor_ventas_completadas = compras.filter(estado='completada').aggregate(total=models.Sum('monto'))['total'] or 0
    valor_ventas_pendientes = compras.filter(estado='pendiente').aggregate(total=models.Sum('monto'))['total'] or 0
    valor_comision = sum([c.comision for c in compras])
    return render(request, 'influencer/dashboard.html', {
        'profile': profile,
        'compras': compras,
        'referidos_pendiente': referidos_pendiente,
        'referidos_completado': referidos_completado,
        'valor_ventas_completadas': valor_ventas_completadas,
        'valor_ventas_pendientes': valor_ventas_pendientes,
        'comision_pendiente': comision_pendiente,
        'comision_completada': comision_completada,
        'coupon_code': profile.coupon_code,
    })


@login_required
def solicitar_retiro(request):
    profile = getattr(request.user, 'influencer_profile', None)
    if not profile:
        return redirect('influencer_suscribete')
    
    messages.success(request, 'Solicitud de retiro enviada. Pronto nos pondremos en contacto.')
    return redirect('influencer_dashboard')

@login_required
def quitar_suscripcion(request):
    profile = getattr(request.user, 'influencer_profile', None)
    if profile:
        profile.delete()
        messages.success(request, 'Has cancelado tu suscripción de influencer.')
    return redirect('/')
