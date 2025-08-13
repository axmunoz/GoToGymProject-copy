from django.db import models
from django.conf import settings
from products.models import Product

class CarritoHistorial(models.Model):
    def get_total(self):
        total = 0
        for item in self.items.all():
            # Usa el precio con descuento si existe
            precio = item.product.discounted_price if item.product.discounted_price else item.product.price
            total += precio * item.cantidad
        return total

    def get_num_productos(self):
        return sum(item.cantidad for item in self.items.all())
    ESTADO_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
    )
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='carritos_historial')
    cupon_code = models.CharField(max_length=32, blank=True, null=True, help_text="Cupón de descuento usado, si aplica.")
    total_pagar = models.PositiveIntegerField(default=0, help_text="Total a pagar calculado en el carrito.")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f"Carrito de {self.usuario} - {self.estado} - {self.fecha_creacion.strftime('%Y-%m-%d %H:%M')}"

class CarritoHistorialItem(models.Model):
    carrito = models.ForeignKey(CarritoHistorial, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    talla = models.CharField(max_length=4, blank=True, null=True)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.cantidad}"
