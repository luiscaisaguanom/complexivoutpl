from django.urls import path
from .views import ReclamosView, ReclamosNew
from .reclamos import reporte_reclamos


urlpatterns = [
    path('quejas/new',ReclamosNew.as_view(), name='quejas_new'),
    path('quejas/',ReclamosView.as_view(), name='quejas_list'),
    path('quejas/listado',reporte_reclamos, name='quejas_print_all')

   

]