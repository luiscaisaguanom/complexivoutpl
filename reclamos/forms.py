from urllib import request
from django import forms
from django.urls import reverse
from .models import Reclamos
from dependencias.models import Circuito, Subcircuito
from dependencias.urls import *

class ReclamosForm(forms.ModelForm):

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 20px;'})
    )

    apellido = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'})
    )

    detalles = forms.CharField(
    widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'})
    )

    contacto = forms.CharField(
    widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'})
    )

    tipo = forms.ChoiceField(
    choices=[('reclamo', 'Reclamo'), ('sugerencia', 'Sugerencia')],
    widget=forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'})
    )



    class Meta:
        model = Reclamos
        fields = ['circuito', 'subcircuito', 'tipo', 'detalles', 'contacto', 'nombre', 'apellido']

    widgets = {
        'circuito': forms.Select(attrs={'class': 'form-control'}),
        'subcircuito': forms.Select(attrs={'class': 'form-control'}),
        'tipo': forms.Select(attrs={'class': 'form-control'}),
        'detalle': forms.Textarea(attrs={'class': 'form-control', 'cols': 80, 'rows': 3}),
        'contacto': forms.TextInput(attrs={'class': 'form-control'}),
        'nombres': forms.TextInput(attrs={'class': 'form-control'}),
        'apellidos': forms.TextInput(attrs={'class': 'form-control'}),

    }
    

    def __init__(self, *args, **kwargs):
        super(ReclamosForm, self).__init__(*args, **kwargs)
        
        # Configurar campo circuito como ModelChoiceField
        self.fields['circuito'].queryset = Circuito.objects.all()
        self.fields['circuito'].widget.attrs['class'] = 'form-control select2'
        
        # Configurar campo subcircuito como ModelChoiceField
        self.fields['subcircuito'].queryset = Subcircuito.objects.all()  # Inicialmente vacío
        self.fields['subcircuito'].widget.attrs['class'] = 'form-control select2'

        # Añadir un atributo de datos para almacenar la URL de la vista AJAX
        self.fields['subcircuito'].widget.attrs['data-url'] = '{% url "dependencias:subcircuito_list" %}'


    def clean(self):
        cleaned_data = super().clean()
        circuito = cleaned_data.get('circuito')
        if circuito:
            # Filtrar opciones de subcircuito según el circuito seleccionado
            self.fields['subcircuito'].queryset = Subcircuito.objects.filter(circuito=circuito)
        return cleaned_data