from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
import random

from register.models import CustomUser
from register.serializers import RegisterSerializer, VerifyCodeSerializer, ProfileUpdateSerializer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        name = request.data.get("name")
        surname = request.data.get("surname")
        email = request.data.get("email")
        phone = request.data.get("phone")

        if CustomUser.objects.filter(email=email).exists():
            return Response({"email": "This email is already registered."}, status=status.HTTP_400_BAD_REQUEST)

        if CustomUser.objects.filter(phone=phone).exists():
            return Response({"phone": "This phone number is already registered."}, status=status.HTTP_400_BAD_REQUEST)

        verification_code = random.randint(100000, 999999)
        send_mail(
            "Tasdiqlash kodingiz",
            f"Sizning tasdiqlash kodingiz: {verification_code}",
            "admin@example.com",
            [email],
            fail_silently=False,
        )

        request.session["verification_code"] = verification_code
        request.session["user_data"] = {"name": name, "surname": surname, "email": email, "phone": phone}

        return Response({"message": "Verification code sent to email."}, status=status.HTTP_200_OK)


class VerifyCodeView(generics.CreateAPIView):
    serializer_class = VerifyCodeSerializer

    def post(self, request):
        entered_code = request.data.get("code")
        saved_code = request.session.get("verification_code")
        user_data = request.session.get("user_data")

        if not saved_code or str(entered_code) != str(saved_code):
            del request.session["verification_code"]  # Noto‘g‘ri kiritganda sessiyani tozalash
            return Response({"error": "Invalid verification code."}, status=status.HTTP_400_BAD_REQUEST)

        if not user_data:
            return Response({"error": "User session expired or not found."}, status=status.HTTP_400_BAD_REQUEST)

        user = CustomUser.objects.create_user(
            email=user_data["email"],
            phone=user_data["phone"],
            name=user_data["name"],
            surname=user_data["surname"],
            password="defaultpassword123",
        )

        request.session.flush()  # Butun sessionni tozalash
        return Response({"message": "Account successfully verified. You can now log in."}, status=status.HTTP_200_OK)


class ProfileUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user  # Hozirgi foydalanuvchini olish

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True  # Faqat yuborilgan maydonlarni yangilash
        return super().update(request, *args, **kwargs)

