from django.urls import path
from .views import PersonalView, PersonalNew, PersonalEdit, personal_inactivate

urlpatterns = [
    path('personal/',PersonalView.as_view(), name='personal_list'),
    path('personal/new',PersonalNew.as_view(), name='personal_new'),
    path('personal/edit/<int:pk>',PersonalEdit.as_view(), name='personal_edit'),
    path('personal/inactivate/<int:id>',personal_inactivate, name='personal_inactivate'),

]