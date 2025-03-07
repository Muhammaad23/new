from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Doctor, Appointment, Payment

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ("id", "username", "email", "phone_number", "is_doctor", "is_staff", "is_active")
    search_fields = ("username", "email", "phone_number")
    list_filter = ("is_doctor", "is_staff", "is_active")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("phone_number", "is_doctor")}),
    )

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "specialization", "rating")
    search_fields = ("user__username", "specialization")
    list_filter = ("specialization",)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "doctor", "patient", "date", "time", "price", "status")
    search_fields = ("doctor__user__username", "patient__username")
    list_filter = ("date", "status")

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "appointment", "amount", "payment_method", "card_number", "paid")
    search_fields = ("appointment__doctor__user__username", "appointment__patient__username", "card_number")
    list_filter = ("payment_method", "paid")
