from django import forms

from incidences.models import Incidence


class IncidenceForm(forms.ModelForm):
    class Meta:
        model = Incidence
        fields = ['name', 'description', 'risk', 'causes', 'effects']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Incidencia'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'risk': forms.Select(attrs={'class': 'form-select'}),
            'causes': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'effects': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }
        labels = {
            'name': '',
            'description': 'Descripción del evento',
            'risk': 'Riesgo asociado',
            'causes': 'Causas manifestadas',
            'effects': 'Consecuencias manifestadas',
        }
