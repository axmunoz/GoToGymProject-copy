
from django.contrib import admin
from .models import Product, ProductCategory, Brand, ProductImage, ProductVideo


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "description"]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ["name", "description"]
    list_display = ["name", "category", "price", "stock"]
    list_filter = ["category"]
    autocomplete_fields = ["category"]

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name"]

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ["product", "image"]

@admin.register(ProductVideo)
class ProductVideoAdmin(admin.ModelAdmin):
    list_display = ["product", "video"]
