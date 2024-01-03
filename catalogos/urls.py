from django.urls import path
from .views import RangoView, RangoNew, RangoEdit, rango_inactivate, \
                    TipoVehiculoView, TipoVehiculoNew, TipoVehiculoEdit, tipovehiculo_inactivate, \
                    TipoMantenimientoView, TipoMantenimientoNew, TipoMantenimientoEdit, tipomantenimiento_inactivate

urlpatterns = [
    #url para rango
    path('rango/',RangoView.as_view(), name='rango_list'),
    path('rango/new',RangoNew.as_view(), name='rango_new'),
    path('rango/edit/<int:pk>',RangoEdit.as_view(), name='rango_edit'),
    path('rango/inactivate/<int:id>',rango_inactivate, name='rango_inactivate'),

    #url para tipo de vehiculo
    path('tipovehiculo/',TipoVehiculoView.as_view(), name='tipovehiculo_list'),
    path('tipovehiculo/new',TipoVehiculoNew.as_view(), name='tipovehiculo_new'),
    path('tipovehiculo/edit/<int:pk>',TipoVehiculoEdit.as_view(), name='tipovehiculo_edit'),
    path('tipovehiculo/inactivate/<int:id>',tipovehiculo_inactivate, name='tipovehiculo_inactivate'),

    #url para tipo de mantenimiento
    path('tipomantenimiento/',TipoMantenimientoView.as_view(), name='tipomantenimiento_list'),
    path('tipomantenimiento/new',TipoMantenimientoNew.as_view(), name='tipomantenimiento_new'),
    path('tipomantenimiento/edit/<int:pk>',TipoMantenimientoEdit.as_view(), name='tipomantenimiento_edit'),
    path('tipomantenimiento/inactivate/<int:id>',tipomantenimiento_inactivate, name='tipomantenimiento_inactivate'),
]