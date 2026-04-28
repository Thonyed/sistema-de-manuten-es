from django import forms
from .models import Escada

class EscadaForm(forms.ModelForm):
    class Meta:
        model = Escada
        fields = '__all__'
        widgets = {
            'problema': forms.Textarea(attrs={
                'rows': 4,
                'cols': 50,
                'placeholder': 'Descreva o problema da escada...'
            }),
        }