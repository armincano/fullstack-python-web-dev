from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']
        widgets = {
            'marca': forms.Select(attrs={'class': 'form-select'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_carroceria': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_motor': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
        }