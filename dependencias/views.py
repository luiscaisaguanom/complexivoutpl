from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Zona, Provincia
from .forms import ZonaForm, ProvinciaForm
from django.urls import reverse_lazy

# Create your views here.
class ZonaView(LoginRequiredMixin, generic.ListView):
    model = Zona
    template_name = "dependencias/zona_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class ZonaNew(LoginRequiredMixin, generic.CreateView):
    model = Zona
    template_name = "dependencias/zona_form.html"
    context_object_name = "obj"
    form_class = ZonaForm
    success_url = reverse_lazy("dependencias:zona_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ZonaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Zona
    template_name = "dependencias/zona_form.html"
    context_object_name = "obj"
    form_class = ZonaForm
    success_url = reverse_lazy("dependencias:zona_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class ZonaDel(LoginRequiredMixin, generic.DeleteView):
    model = Zona
    template_name = 'dependencias/catalogos_del.html'
    context_object_name = "obj"
    success_url = reverse_lazy("dependencias:zona_list")

class ProvinciaView(LoginRequiredMixin, generic.ListView):
    model = Provincia
    template_name = "dependencias/provincia_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class ProvinciaNew(LoginRequiredMixin, generic.CreateView):
    model = Provincia
    template_name = "dependencias/provincia_form.html"
    context_object_name = "obj"
    form_class = ProvinciaForm
    success_url = reverse_lazy("dependencias:provincia_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class ProvinciaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Provincia
    template_name = "dependencias/provincia_form.html"
    context_object_name = "obj"
    form_class = ProvinciaForm
    success_url = reverse_lazy("dependencias:provincia_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
class ProvinciaDel(LoginRequiredMixin, generic.DeleteView):
    model = Provincia
    template_name = 'dependencias/catalogos_del.html'
    context_object_name = "obj"
    success_url = reverse_lazy("dependencias:zona_list")