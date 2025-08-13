from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    def clean_content(self):
        data = self.cleaned_data.get('content', '')
        # Permitir HTML, pero considerar vacío si solo hay <p><br></p>
        if not data or data.strip() == '' or data.strip() == '<p><br></p>':
            raise forms.ValidationError('Este campo es requerido.')
        return data
    class Meta:
        model = Post
        fields = ['title', 'author', 'category', 'excerpt', 'content', 'featured']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input w-full'}),
            'author': forms.Select(attrs={'class': 'form-select w-full'}),
            'category': forms.Select(attrs={'class': 'form-select w-full'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-textarea w-full', 'rows': 2}),
            # 'content' widget eliminado para evitar conflicto con el editor WYSIWYG
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Eliminar el widget del campo content para que no se renderice el textarea
        self.fields['content'].widget = forms.HiddenInput()
