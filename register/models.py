from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, related_name="customuser_groups_api", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions_api", blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class VerificationCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="verification_codes")
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.code}"