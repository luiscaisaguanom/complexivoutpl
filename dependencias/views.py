from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from .models import Zona, Provincia, Distrito, Canton, Circuito, Subcircuito
from .forms import ZonaForm, ProvinciaForm, DistritoForm, CantonForm, CircuitoForm, SubcircuitoForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

# Create your views here.
#vista de clases para listar zonas
class ZonaView(LoginRequiredMixin, ListView):
    model = Zona
    template_name = "dependencias/zona_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

#vista de clases para crear zonas
class ZonaNew(LoginRequiredMixin, CreateView):
    model = Zona
    template_name = "dependencias/zona_form.html"
    context_object_name = "obj"
    form_class = ZonaForm
    success_url = reverse_lazy("dependencias:zona_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

# vista de clases para editar zonas
class ZonaEdit(LoginRequiredMixin, UpdateView):
    model = Zona
    template_name = "dependencias/zona_form.html"
    context_object_name = "obj"
    form_class = ZonaForm
    success_url = reverse_lazy("dependencias:zona_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

#vista de clases para borrar zonas
class ZonaDel(LoginRequiredMixin, DeleteView):
    model = Zona
    template_name = 'dependencias/dependencias_delete.html'
    context_object_name = "obj"
    success_url = reverse_lazy("dependencias:zona_list")

# Vista de funciones para inactivar zonas
def zona_inactivate(request, id):
    zona = Zona.objects.filter(pk=id).first()
    contexto = {}
    template_name = "dependencias/dependencias_delete.html "

    if not zona:
        return redirect("dependencias:zona_list")
    
    if request.method=='GET':
        contexto = {'obj':zona}

    if request.method=='POST':
        zona.estado = False
        zona.save()
        return redirect("dependencias:zona_list")

    return render(request, template_name, contexto)

#vista para listas provincias
class ProvinciaView(LoginRequiredMixin, ListView):
    model = Provincia
    template_name = "dependencias/provincia_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

#vista para crear provincias
class ProvinciaNew(LoginRequiredMixin, CreateView):
    model = Provincia
    template_name = "dependencias/provincia_form.html"
    context_object_name = "obj"
    form_class = ProvinciaForm
    success_url = reverse_lazy("dependencias:provincia_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
#vista para editar provincias
class ProvinciaEdit(LoginRequiredMixin, UpdateView):
    model = Provincia
    template_name = "dependencias/provincia_form.html"
    context_object_name = "obj"
    form_class = ProvinciaForm
    success_url = reverse_lazy("dependencias:provincia_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
#vista para eliminar provincias
class ProvinciaDel(LoginRequiredMixin, DeleteView):
    model = Provincia
    template_name = 'dependencias/catalogos_delete.html'
    context_object_name = "obj"
    success_url = reverse_lazy("dependencias:zona_list")

# Vista de funciones para inactivar provincias
def provincia_inactivate(request, id):
    provincia = Provincia.objects.filter(pk=id).first()
    contexto = {}
    template_name = "dependencias/dependencias_delete.html "

    if not provincia:
        return redirect("dependencias:provincia_list")
    
    if request.method=='GET':
        contexto = {'obj':provincia}

    if request.method=='POST':
        provincia.estado = False
        provincia.save()
        return redirect("dependencias:provincia_list")

    return render(request, template_name, contexto)

#vista para listar distritos
class DistritoView(LoginRequiredMixin, ListView):
    model = Distrito
    template_name = "dependencias/distrito_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

#vista para crear distritos
class DistritoNew(LoginRequiredMixin, CreateView):
    model = Distrito
    template_name = "dependencias/distrito_form.html"
    context_object_name = "obj"
    form_class = DistritoForm
    success_url = reverse_lazy("dependencias:distrito_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
#vista para editar distritos
class DistritoEdit(LoginRequiredMixin, UpdateView):
    model = Distrito
    template_name = "dependencias/distrito_form.html"
    context_object_name = "obj"
    form_class = DistritoForm
    success_url = reverse_lazy("dependencias:distrito_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
#vista para eliminar provincias
class DistritoDel(LoginRequiredMixin, DeleteView):
    model = Distrito
    template_name = 'dependencias/dependencias_delete.html'
    context_object_name = "obj"
    success_url = reverse_lazy("dependencias:distrito_list")

# Vista de funciones para inactivar provincias
def distrito_inactivate(request, id):
    distrito = Distrito.objects.filter(pk=id).first()
    contexto = {}
    template_name = "dependencias/dependencias_delete.html "

    if not distrito:
        return redirect("dependencias:distrito_list")
    
    if request.method=='GET':
        contexto = {'obj':distrito}

    if request.method=='POST':
        distrito.estado = False
        distrito.save()
        return redirect("dependencias:distrito_list")

    return render(request, template_name, contexto)

#Vistas para Cantones
class CantonView(LoginRequiredMixin, ListView):
    template_name = "dependencias/canton_list.html"
    login_url = 'bases:login'
    model = Canton
    context_object_name = "obj"

class CantonNew(LoginRequiredMixin, CreateView):
    model = Canton
    template_name = "dependencias/canton_form.html"
    context_object_name = "obj"
    form_class = CantonForm
    success_url = reverse_lazy("dependencias:canton_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class CantonEdit(LoginRequiredMixin,UpdateView):
    model = Canton
    template_name = "dependencias/canton_form.html"
    context_object_name = "obj"
    form_class = CantonForm
    success_url = reverse_lazy("dependencias:canton_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
# Vista de función para inactivar canton
def canton_inactivate(request, id):
    canton = Canton.objects.filter(pk=id).first()
    contexto = {}
    template_name = "dependencias/dependencias_delete.html "

    if not canton:
        return redirect("dependencias:canton_list")
    
    if request.method=='GET':
        contexto = {'obj':canton}

    if request.method=='POST':
        canton.estado = False
        canton.save()
        return redirect("dependencias:canton_list")

    return render(request, template_name, contexto)

#Vistas para Circuitos
class CircuitoView(LoginRequiredMixin, ListView):
    template_name = "dependencias/circuito_list.html"
    login_url = 'bases:login'
    model = Circuito
    context_object_name = "obj"

class CircuitoNew(LoginRequiredMixin, CreateView):
    model = Circuito
    template_name = "dependencias/circuito_form.html"
    context_object_name = "obj"
    form_class = CircuitoForm
    success_url = reverse_lazy("dependencias:circuito_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class CircuitoEdit(LoginRequiredMixin,UpdateView):
    model = Circuito
    template_name = "dependencias/circuito_form.html"
    context_object_name = "obj"
    form_class = CircuitoForm
    success_url = reverse_lazy("dependencias:circuito_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
# Vista de función para inactivar canton
def circuito_inactivate(request, id):
    circuito = Circuito.objects.filter(pk=id).first()
    contexto = {}
    template_name = "dependencias/dependencias_delete.html "

    if not circuito:
        return redirect("dependencias:circuito_list")
    
    if request.method=='GET':
        contexto = {'obj':circuito}

    if request.method=='POST':
        circuito.estado = False
        circuito.save()
        return redirect("dependencias:circuito_list")

    return render(request, template_name, contexto)


#Vistas para Subcircuitos
class SubcircuitoView(LoginRequiredMixin, ListView):
    template_name = "dependencias/subcircuito_list.html"
    login_url = 'bases:login'
    model = Subcircuito
    context_object_name = "obj"

class SubcircuitoNew(LoginRequiredMixin, CreateView):
    model = Subcircuito
    template_name = "dependencias/subcircuito_form.html"
    context_object_name = "obj"
    form_class = SubcircuitoForm
    success_url = reverse_lazy("dependencias:subcircuito_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class SubcircuitoEdit(LoginRequiredMixin,UpdateView):
    model = Subcircuito
    template_name = "dependencias/subcircuito_form.html"
    context_object_name = "obj"
    form_class = SubcircuitoForm
    success_url = reverse_lazy("dependencias:subcircuito_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
# Vista de función para inactivar canton
def subcircuito_inactivate(request, id):
    subcircuito = Subcircuito.objects.filter(pk=id).first()
    contexto = {}
    template_name = "dependencias/dependencias_delete.html "

    if not subcircuito:
        return redirect("dependencias:subcircuito_list")
    
    if request.method=='GET':
        contexto = {'obj':subcircuito}

    if request.method=='POST':
        subcircuito.estado = False
        subcircuito.save()
        return redirect("dependencias:subcircuito_list")

    return render(request, template_name, contexto)
