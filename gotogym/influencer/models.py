from django.db import models
from django.conf import settings
import uuid
import random
import string
from products.models import Product

def generate_coupon_code(length=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

class InfluencerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='influencer_profile')
    coupon_code = models.CharField(max_length=12, unique=True, default=generate_coupon_code)
    commission_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_referred = models.PositiveIntegerField(default=0)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    commission_percent = models.DecimalField(max_digits=5, decimal_places=2, default=5)  

    def __str__(self):
        return f"Influencer: {self.user.email} ({self.coupon_code})"


class CompraReferida(models.Model):
    comision = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def calcular_comision(self):
        porcentaje = float(self.influencer.commission_percent)
        if porcentaje <= 0:
            porcentaje = 5.0
        return round(float(self.monto) * porcentaje / 100, 2)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='compras_referidas', null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    influencer = models.ForeignKey(InfluencerProfile, on_delete=models.CASCADE, related_name='compras_generadas')
    productos = models.ManyToManyField(Product)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='completada')
    carrito_historial = models.ForeignKey('carrito.CarritoHistorial', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Compra referida de {self.usuario} por {self.monto} para {self.influencer.user.username}"
