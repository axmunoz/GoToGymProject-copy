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
