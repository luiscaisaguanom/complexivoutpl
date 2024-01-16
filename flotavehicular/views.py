from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import FlotaVehicular
from .forms import FlotaVehicularForm

# Create your views here.
# Listar Flota vehicular
class FlotaVehicularView(LoginRequiredMixin, generic.ListView):
    model = FlotaVehicular
    template_name = "flotavehicular/flotavehicular_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

# Crear Flota Vehicular
class FlotaVehicularNew(LoginRequiredMixin, generic.CreateView):
    model = FlotaVehicular
    template_name = "flotavehicular/flotavehicular_form.html"
    context_object_name = "obj"
    form_class = FlotaVehicularForm
    success_url = reverse_lazy("flotavehicular:flotavehicular_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
# Editar Flota Vehicular
class FlotaVehicularEdit(LoginRequiredMixin, generic.UpdateView):
    model = FlotaVehicular
    template_name = "flotavehicular/flotavehicular_form.html"
    context_object_name = "obj"
    form_class = FlotaVehicularForm
    success_url = reverse_lazy("flotavehicular:flotavehicular_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
def flotavehicular_inactivate(request, id):
    flotavehicular = FlotaVehicular.objects.filter(pk=id).first()
    contexto = {}
    template_name = "flotavehicular/flotavehicular_del.html"

    if not flotavehicular:
        return redirect("flotavehicular:flotavehicular_list")
    
    if request.method == 'GET':
        contexto = {'obj': flotavehicular}

    if request.method == 'POST':
        flotavehicular.estado = False
        flotavehicular.save()
        return redirect("flotavehicular:flotavehicular_list")

    return render(request, template_name, contexto)