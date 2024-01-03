
from django.urls import path
from .views import ZonaView, ZonaNew, ZonaEdit, ZonaDel, \
                    ProvinciaView, ProvinciaNew, ProvinciaEdit, ProvinciaDel

urlpatterns = [
    path('zonas/',ZonaView.as_view(), name='zona_list'),
    path('zonas/new',ZonaNew.as_view(), name='zona_new'),
    path('zonas/edit/<int:pk>',ZonaEdit.as_view(), name='zona_edit'),
    path('zonas/delete/<int:pk>',ZonaDel.as_view(), name='zona_del'),

    path('provincia/',ProvinciaView.as_view(), name='provincia_list'),
    path('provincia/new',ProvinciaNew.as_view(), name='provincia_new'),
    path('provincia/edit/<int:pk>',ProvinciaEdit.as_view(), name='provincia_edit'),
    path('provincia/delete/<int:pk>',ProvinciaDel.as_view(), name='provincia_del'),
]