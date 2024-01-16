
from django.urls import path
from .views import ZonaView, ZonaNew, ZonaEdit, ZonaDel, zona_inactivate, \
                    ProvinciaView, ProvinciaNew, ProvinciaEdit, ProvinciaDel, provincia_inactivate, \
                    DistritoView, DistritoNew, DistritoEdit, DistritoDel, distrito_inactivate, \
                    CantonView, CantonNew, CantonEdit, canton_inactivate, \
                    CircuitoView, CircuitoNew, CircuitoEdit, circuito_inactivate, \
                    SubcircuitoView, SubcircuitoNew, SubcircuitoEdit, subcircuito_inactivate

urlpatterns = [
    path('zonas/',ZonaView.as_view(), name='zona_list'),
    path('zonas/new',ZonaNew.as_view(), name='zona_new'),
    path('zonas/edit/<int:pk>',ZonaEdit.as_view(), name='zona_edit'),
    path('zonas/delete/<int:pk>',ZonaDel.as_view(), name='zona_del'),
    path('zonas/inactivate/<int:id>',zona_inactivate, name='zona_inactivate'),

    path('provincia/',ProvinciaView.as_view(), name='provincia_list'),
    path('provincia/new',ProvinciaNew.as_view(), name='provincia_new'),
    path('provincia/edit/<int:pk>',ProvinciaEdit.as_view(), name='provincia_edit'),
    path('provincia/delete/<int:pk>',ProvinciaDel.as_view(), name='provincia_del'),
    path('provincia/inactivate/<int:id>',provincia_inactivate, name='provincia_inactivate'),

    path('distrito/',DistritoView.as_view(), name='distrito_list'),
    path('distrito/new',DistritoNew.as_view(), name='distrito_new'),
    path('distrito/edit/<int:pk>',DistritoEdit.as_view(), name='distrito_edit'),
    path('distrito/delete/<int:pk>',DistritoDel.as_view(), name='distrito_del'),
    path('distrito/inactivate/<int:id>',distrito_inactivate, name='distrito_inactivate'),

    path('canton/',CantonView.as_view(), name='canton_list'),
    path('canton/new',CantonNew.as_view(), name='canton_new'),
    path('canton/edit/<int:pk>',CantonEdit.as_view(), name='canton_edit'),
    path('canton/inactivate/<int:id>',canton_inactivate, name='canton_inactivate'),

    path('circuito/',CircuitoView.as_view(), name='circuito_list'),
    path('circuito/new',CircuitoNew.as_view(), name='circuito_new'),
    path('circuito/edit/<int:pk>',CircuitoEdit.as_view(), name='circuito_edit'),
    path('circuito/inactivate/<int:id>',circuito_inactivate, name='circuito_inactivate'),

    path('subcircuito/',SubcircuitoView.as_view(), name='subcircuito_list'),
    path('subcircuito/new',SubcircuitoNew.as_view(), name='subcircuito_new'),
    path('subcircuito/edit/<int:pk>',SubcircuitoEdit.as_view(), name='subcircuito_edit'),
    path('subcircuito/inactivate/<int:id>',subcircuito_inactivate, name='subcircuito_inactivate'),
]