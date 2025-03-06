from rest_framework import serializers
from .models import CustomUser, Doctor, Appointment, Payment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number', 'is_doctor']


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Doctor
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    patient = UserSerializer()

    class Meta:
        model = Appointment
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    appointment = AppointmentSerializer()

    class Meta:
        model = Payment
        fields = '__all__'
