from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from .models import Reclamos
from .forms import ReclamosForm
from django.urls import reverse_lazy


# Create your views here.
#Vista para crear Reclamos y sugerencias
class ReclamosNew(CreateView):

    model = Reclamos
    template_name = "reclamos/reclamos_new.html"
    context_object_name = "obj"
    form_class = ReclamosForm
    success_url = reverse_lazy("bases:login")
    login_url = 'bases:login'


    def form_valid(self, form):
        return super().form_valid(form)
    
# Vistas para Reclamos y Sugerencias
class ReclamosView(LoginRequiredMixin, ListView):
    template_name = "reclamos/reclamos_list.html"
    login_url = 'bases:login'
    model = Reclamos
    context_object_name = "obj"
