
from django.db import models
# Modelo para tallas globales
class Talla(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.nombre
# --- STOCK POR TALLA ---

class ProductStock(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='stocks')
    talla = models.CharField(max_length=20)  # Permite tallas personalizadas
    cantidad = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('product', 'talla')
    def __str__(self):
        return f"{self.product.name} - {self.talla}: {self.cantidad}"
from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=4)
    discount = models.PositiveIntegerField(default=0, help_text="Porcentaje de descuento")
    stock = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=False)
    discounted_price = models.DecimalField(max_digits=12, decimal_places=4, default=0)

    def save(self, *args, **kwargs):
        # Si no hay descuento, el precio con descuento es igual al precio
        from decimal import Decimal, InvalidOperation
        try:
            discount = Decimal(self.discount)
        except (TypeError, ValueError, InvalidOperation):
            discount = Decimal('0')
        # Si el descuento es None, negativo o 0, el precio con descuento es igual al precio
        if discount is None or discount <= 0:
            self.discounted_price = self.price
        else:
            # Si el descuento es 100 o más, el precio con descuento es 0 (no negativo)
            if discount >= 100:
                self.discounted_price = Decimal('0.00')
            else:
                self.discounted_price = (self.price * (Decimal('1.0') - (discount / Decimal('100')))).quantize(Decimal('0.01'))

        # Actualizar el stock total sumando todas las cantidades de ProductStock
        if self.pk:
            try:
                total_stock = self.stocks.aggregate(total=models.Sum('cantidad'))['total']
                self.stock = total_stock or 0
            except Exception:
                pass
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# Permite hasta 7 imágenes por producto
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/images/')

    def __str__(self):
        return f"Imagen de {self.product.name}"

# Permite 1 video por producto
class ProductVideo(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='video')
    video = models.FileField(upload_to='products/videos/')

    def __str__(self):
        return f"Video de {self.product.name}"
