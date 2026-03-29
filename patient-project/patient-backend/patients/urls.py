from django.urls import path
from .import views

urlpatterns = [
    path('add/', views.add_patient, name='add_patient'),
    path('<int:patient_id>/', views.get_patient, name='get_patient'),   
    path('list-patients/', views.list_patients, name='list_patients'),  
]