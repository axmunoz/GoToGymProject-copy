
from django import forms
from .models import Product, ProductImage, ProductVideo

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'brand', 'description', 'price', 'discount', 'stock', 'featured']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

# Formulario para múltiples imágenes
class ProductImageForm(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = ProductImage
        fields = ['image']

# Formulario para video
class ProductVideoForm(forms.ModelForm):
    class Meta:
        model = ProductVideo
        fields = ['video']
