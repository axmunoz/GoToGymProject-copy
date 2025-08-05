
from django import forms
from .models import Product, ProductImage, ProductVideo

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'brand', 'description', 'price', 'discount', 'stock', 'featured']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_price(self):
        from decimal import Decimal, InvalidOperation
        price = self.cleaned_data['price']
        if isinstance(price, str):
            price = price.replace('.', '')
            price = price.replace(',', '.')
        try:
            return Decimal(price)
        except (InvalidOperation, ValueError, TypeError):
            raise forms.ValidationError('Precio inválido')

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
