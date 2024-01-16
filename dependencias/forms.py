from django import forms
from .models import Zona, Provincia, Distrito, Canton, Circuito, Subcircuito

class ZonaForm(forms.ModelForm):
    class Meta:
        model = Zona
        fields = ['codigo','nombre','estado']
        labels = {'codigo':"Código de Zona",'nombre':"Nombre de Zona",'estado':"Estado"}
        widget = {'codigo': forms.TextInput,'nombre': forms.TextInput}

    def __ini__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class ProvinciaForm(forms.ModelForm):
    zona = forms.ModelChoiceField(
        queryset=Zona.objects.filter(estado=True).order_by('codigo'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Provincia
        fields = ['zona', 'codigo', 'nombre', 'estado']
        labels = {'codigo': "Código", 'nombre': "Nombre", 'estado': "Estado"}
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el código'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['zona'].empty_label = "Zona"


class DistritoForm(forms.ModelForm):
    provincia = forms.ModelChoiceField(
        queryset=Provincia.objects.filter(estado=True).order_by('nombre'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Distrito
        fields = ['provincia', 'codigo', 'nombre', 'estado']
        labels = {'codigo': "Código", 'nombre': "Nombre", 'estado': "Estado"}
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el código'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['provincia'].empty_label = "Provincia"

class CantonForm(forms.ModelForm):
    distrito = forms.ModelChoiceField(
        queryset=Distrito.objects.filter(estado=True).order_by('nombre'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Canton
        fields = ['distrito', 'codigo', 'nombre', 'estado']
        labels = {'codigo': "Código", 'nombre': "Nombre", 'estado': "Estado"}
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el código'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['distrito'].empty_label = "Distrito"

class CircuitoForm(forms.ModelForm):
    canton = forms.ModelChoiceField(
        queryset=Canton.objects.filter(estado=True).order_by('nombre'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Circuito
        fields = ['canton', 'codigo', 'nombre', 'estado']
        labels = {'codigo': "Código", 'nombre': "Nombre", 'estado': "Estado"}
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el código'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['canton'].empty_label = "Canton"

class SubcircuitoForm(forms.ModelForm):
    circuito = forms.ModelChoiceField(
        queryset=Circuito.objects.filter(estado=True).order_by('nombre'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Subcircuito
        fields = ['circuito', 'codigo', 'nombre', 'estado']
        labels = {'codigo': "Código", 'nombre': "Nombre", 'estado': "Estado"}
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el código'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['circuito'].empty_label = "Circuito"