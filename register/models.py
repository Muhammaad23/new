from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, phone, name, surname, password=None, **extra_fields):
        if not email:
            raise ValueError("Email field is required")
        if not phone:
            raise ValueError("Phone field is required")

        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, name=name, surname=surname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, name, surname, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, phone, name, surname, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)  # Telefon raqam unique bo'lishi kerak
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone", "name", "surname"]  # `email` bu yerda kerak emas

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.name} {self.surname} ({self.email})"
