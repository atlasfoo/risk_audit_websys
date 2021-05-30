from django import forms

from risk.models import Risk, Cause, Effect


class RiskForm(forms.ModelForm):
    class Meta:
        model = Risk
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Riesgo'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': '',
            'description': 'Descripción del riesgo',
        }


class CauseForm(forms.ModelForm):
    class Meta:
        model = Cause
        fields = ['name', 'description', 'risk']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Riesgo'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'risk': forms.Select(attrs={'class': 'form-select'})
        }
        labels = {
            'name': '',
            'description': 'Descripción del riesgo',
            'risk': 'Riesgo asociado'
        }


# EffectForm
class EffectForm(forms.ModelForm):
    class Meta:
        model = Effect
        fields = ['name', 'description', 'economic_loss', 'risk']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Riesgo'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'economic_loss': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Costo económico'}),
            'risk': forms.Select(attrs={'class': 'form-select'})
        }
        labels = {
            'name': '',
            'description': 'Descripción del riesgo',
            'economic_loss': '',
            'risk': 'Riesgo asociado'
        }
