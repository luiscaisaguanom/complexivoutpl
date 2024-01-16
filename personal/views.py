from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Personal
from django.views import generic
from .forms import PersonalForm

# Create your views here.
#Listar Personal
class PersonalView(LoginRequiredMixin, generic.ListView):
    model = Personal
    template_name = "personal/personal_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

# Crear Personal
class PersonalNew(LoginRequiredMixin, generic.CreateView):
    model = Personal
    template_name = "personal/personal_form.html"
    context_object_name = "obj"
    form_class = PersonalForm
    success_url = reverse_lazy("personal:personal_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
# Editar Flota Vehicular
class PersonalEdit(LoginRequiredMixin, generic.UpdateView):
    model = Personal
    template_name = "personal/personal_form.html"
    context_object_name = "obj"
    form_class = PersonalForm
    success_url = reverse_lazy("personal:personal_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
def personal_inactivate(request, id):
    personal = Personal.objects.filter(pk=id).first()
    contexto = {}
    template_name = "personal/personal_del.html"

    if not personal:
        return redirect("personal:personal_list")
    
    if request.method == 'GET':
        contexto = {'obj': personal}

    if request.method == 'POST':
        personal.estado = False
        personal.save()
        return redirect("personal:personal_list")

    return render(request, template_name, contexto)
