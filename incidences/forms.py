from django import forms

from controls.models import Control
from incidences.models import Incidence


class IncidenceForm(forms.ModelForm):
    class Meta:
        model = Incidence
        fields = ['name', 'description', 'risk', 'causes', 'effects', 'controls']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Incidencia'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'risk': forms.Select(attrs={'class': 'form-select'}),
            'causes': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'effects': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'controls': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }
        labels = {
            'name': '',
            'description': 'Descripción del evento',
            'risk': 'Riesgo asociado',
            'causes': 'Causas manifestadas',
            'effects': 'Consecuencias manifestadas',
        }
