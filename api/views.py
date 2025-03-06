from rest_framework import generics
from .models import Doctor, Appointment, Payment, CustomUser
from .serializers import DoctorSerializer, AppointmentSerializer, PaymentSerializer, UserSerializer


class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.filter(is_doctor=True)
    serializer_class = UserSerializer

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

# **Uchrashuv API**
class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

# **To‘lov API**
class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
