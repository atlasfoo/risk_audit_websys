from django import forms

from risk.models import Risk


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

# TODO: CauseForm
# TODO: EffectForm

