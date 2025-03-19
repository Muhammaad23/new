# translator/urls.py
from django.urls import path
from .views import TranslateText

urlpatterns = [
    path('translate/', TranslateText.as_view(), name='translate'),
]
