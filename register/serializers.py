from rest_framework import serializers
from register.models import CustomUser
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
import random


User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name', 'surname', 'email', 'phone',]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if CustomUser.objects.filter(phone=validated_data["phone"]).exists():
            raise serializers.ValidationError({"phone": "This phone number is already registered."})

        return CustomUser.objects.create_user(**validated_data)


class VerifyCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=4)


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "surname", "email", "phone"]
        extra_kwargs = {
            "email": {"required": False},
        }

    def validate_email(self, value):
        """Emailni tekshirish"""
        user = self.instance  # Hozirgi foydalanuvchi
        if value and User.objects.filter(email=value).exclude(id=user.id).exists():
            raise serializers.ValidationError("Ushbu email allaqachon ishlatilgan.")
        return value

