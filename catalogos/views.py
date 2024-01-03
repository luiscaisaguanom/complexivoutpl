from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Rango, Tipo_Vehiculo, Tipo_Mantenimiento
from .forms import RangoForm, TipoVehiculoForm, TipoMantenimientoForm
from django.urls import reverse_lazy

# Create your views here.
# Vista  de clase para listar o ver rangos
class RangoView(LoginRequiredMixin, generic.ListView):
    model = Rango
    template_name = "catalogos/rango_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

# Vista de clase para Crear Rangos
class RangoNew(LoginRequiredMixin, generic.CreateView):
    model = Rango
    template_name = "catalogos/rango_form.html"
    context_object_name = "obj"
    form_class = RangoForm
    success_url = reverse_lazy("catalogos:rango_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

# Vista de clase para editar Rangos 
class RangoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Rango
    template_name = "catalogos/rango_form.html"
    context_object_name = "obj"
    form_class = RangoForm
    success_url = reverse_lazy("catalogos:rango_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)    

# Vista de función para inactivar rangos
def rango_inactivate(request, id):
    rango = Rango.objects.filter(pk=id).first()
    contexto = {}
    template_name = "catalogos/catalogo_delete.html "

    if not rango:
        return redirect("catalogos:rango_list")
    
    if request.method=='GET':
        contexto = {'obj':rango}

    if request.method=='POST':
        rango.estado = False
        rango.save()
        return redirect("catalogos:rango_list")

    return render(request, template_name, contexto)

# Vista de clase para listar tipo de vehiculos
class TipoVehiculoView(LoginRequiredMixin, generic.ListView):
    model = Tipo_Vehiculo
    template_name = "catalogos/tipovehiculo_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

# Vista de clase para crear tipo de vehiculos
class TipoVehiculoNew(LoginRequiredMixin, generic.CreateView):
    model = Tipo_Vehiculo
    template_name = "catalogos/tipovehiculo_form.html"
    context_object_name = "obj"
    form_class = TipoVehiculoForm
    success_url = reverse_lazy("catalogos:tipovehiculo_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

# Vista de clase para editar tipo de vehiculos
class TipoVehiculoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Tipo_Vehiculo
    template_name = "catalogos/tipovehiculo_form.html"
    context_object_name = "obj"
    form_class = TipoVehiculoForm
    success_url = reverse_lazy("catalogos:tipovehiculo_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
# Vista de función para inactivar tipo de vehiculos
def tipovehiculo_inactivate(request, id):
    tipovehiculo = Tipo_Vehiculo.objects.filter(pk=id).first()
    contexto = {}
    template_name = "catalogos/catalogo_delete.html "

    if not tipovehiculo:
        return redirect("catalogos:tipovehiculo_list")
    
    if request.method=='GET':
        contexto = {'obj':tipovehiculo}

    if request.method=='POST':
        tipovehiculo.estado = False
        tipovehiculo.save()
        return redirect("catalogos:tipovehiculo_list")

    return render(request, template_name, contexto)
    
# Vista de clase para listar tipo de mantenimientos
class TipoMantenimientoView(LoginRequiredMixin, generic.ListView):
    model = Tipo_Mantenimiento
    template_name = "catalogos/tipomantenimiento_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

# Vista de clase para crear tipo de mantenimiento
class TipoMantenimientoNew(LoginRequiredMixin, generic.CreateView):
    model = Tipo_Mantenimiento
    template_name = "catalogos/tipomantenimiento_form.html"
    context_object_name = "obj"
    form_class = TipoMantenimientoForm
    success_url = reverse_lazy("catalogos:tipomantenimiento_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
# Vista de clase para editar tipo de mantenimiento
class TipoMantenimientoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Tipo_Mantenimiento
    template_name = "catalogos/tipomantenimiento_form.html"
    context_object_name = "obj"
    form_class = TipoMantenimientoForm
    success_url = reverse_lazy("catalogos:tipomantenimiento_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
# Vista de función para inactivar tipo de mantenimiento
def tipomantenimiento_inactivate(request, id):
    tipomantenimiento = Tipo_Mantenimiento.objects.filter(pk=id).first()
    contexto = {}
    template_name = "catalogos/catalogo_delete.html "

    if not tipomantenimiento:
        return redirect("catalogos:tipomantenimiento_list")
    
    if request.method=='GET':
        contexto = {'obj':tipomantenimiento}

    if request.method=='POST':
        tipomantenimiento.estado = False
        tipomantenimiento.save()
        return redirect("catalogos:tipomantenimiento_list")

    return render(request, template_name, contexto)
