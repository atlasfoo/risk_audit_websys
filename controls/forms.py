from django import forms

from controls.models import Control


class ControlForm(forms.ModelForm):
    class Meta:
        model = Control
        fields = ['name', 'description', 'order', 'risk']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Orden de ejecución'}),
            'risk': forms.Select(attrs={'class': 'form-select'})
        }
        labels = {
            'name': '',
            'description': 'Descripción del riesgo',
            'order': '',
            'risk': 'Riesgo asociado'
        }
