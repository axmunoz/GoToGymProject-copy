
from django import forms
from .models import User

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'age', 'weight', 'city', 'height']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'email': forms.EmailInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'phone_number': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'age': forms.NumberInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'weight': forms.NumberInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'city': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'height': forms.NumberInput(attrs={'class': 'w-full border rounded px-3 py-2', 'min': 0, 'max': 300, 'placeholder': 'cm'}),
        }

