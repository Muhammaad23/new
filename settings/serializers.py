from rest_framework import serializers
from .models import UserSettings

class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = ['id', 'language', 'theme', 'user']
