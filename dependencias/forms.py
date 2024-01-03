from django import forms
from .models import Zona, Provincia

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
        queryset=Zona.objects.filter(estado=True)
        .order_by('codigo')
    )
    class Meta:
        model = Provincia
        fields = ['zona','codigo','nombre','estado']
        labels = {'codigo':"Código",'nombre':"Nombre",'estado':"Estado"}
        widget = {'codigo': forms.TextInput,'nombre': forms.TextInput}

    def __ini__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['zona'].empty_label = "Zona"