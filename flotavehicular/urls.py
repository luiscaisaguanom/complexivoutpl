from django.urls import path
from .views import FlotaVehicularView, FlotaVehicularNew, FlotaVehicularEdit, flotavehicular_inactivate

urlpatterns = [

    #url para flota vehicular
    path('flotavehicular/',FlotaVehicularView.as_view(), name='flotavehicular_list'),
    path('flotavehicular/new',FlotaVehicularNew.as_view(), name='flotavehicular_new'),
    path('flotavehicular/edit/<int:pk>',FlotaVehicularEdit.as_view(), name='flotavehicular_edit'),
    path('flotavehicular/inactivate/<int:id>',flotavehicular_inactivate, name='flotavehicular_inactivate'),
]