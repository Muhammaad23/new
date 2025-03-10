from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ("id", "email", "phone", "name", "surname", "is_staff", "is_active")
    list_filter = ("is_active", "is_staff", "is_superuser")  # Filtrlash
    search_fields = ("id", "email", "phone", "name", "surname")  # Qidirish
    ordering = ("id",)  # ID bo‘yicha tartiblash

    fieldsets = (
        ("Basic Info", {"fields": ("email", "phone", "password")}),
        ("Personal Info", {"fields": ("name", "surname")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "phone", "name", "surname", "password1", "password2", "is_staff", "is_active"),
        }),
    )

    filter_horizontal = ("groups", "user_permissions")  # Guruhlar va ruxsatlar

