from django.urls import path
from .views import doctor_list, doctor_detail

urlpatterns = [
    path('doctors/', doctor_list, name='doctor-list'),
    path('doctors/<int:pk>/', doctor_detail, name='doctor-detail'),
]
