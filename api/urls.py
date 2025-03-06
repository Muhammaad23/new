from django.urls import path
from .views import DoctorListCreateView, DoctorDetailView, AppointmentListCreateView, AppointmentDetailView, PaymentListCreateView, PaymentDetailView

urlpatterns = [
    # Shifokorlar
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),

    # Uchrashuvlar
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-list-create'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),

    # To‘lovlar
    path('payments/', PaymentListCreateView.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
]
