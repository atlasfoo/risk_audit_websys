from django import forms

from risk.models import Risk, Cause


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
# TODO: EffectForm

