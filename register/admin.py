from django.contrib import admin
from .models import CustomUser, VerificationCode

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'is_staff', 'is_superuser')

@admin.register(VerificationCode)
class VerificationCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'code', 'created_at')
    search_fields = ('user__email', 'code')
    list_filter = ('created_at',)
