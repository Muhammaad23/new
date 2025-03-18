from django.db import models
from django.conf import settings


class UserSettings(models.Model):
    LANGUAGE_CHOICES = [
        ('uz', 'Uzbek'),
        ('ru', 'Russian'),
        ('en', 'English'),
    ]

    THEME_CHOICES = [
        ('light', 'Kunduzgi rejim'),
        ('dark', 'Tungi rejim'),
    ]

    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='uz')
    theme = models.CharField(max_length=5, choices=THEME_CHOICES, default='light')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.language} - {self.theme}"
