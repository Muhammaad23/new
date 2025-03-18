from django.contrib import admin
from .models import UserSettings

@admin.register(UserSettings)
class UserSettingsAdmin(admin.ModelAdmin):
    list_display = ('user', 'language', 'theme')
    list_filter = ('language', 'theme')
