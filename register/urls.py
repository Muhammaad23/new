from django.urls import path

from register.views import RegisterView, VerifyCodeView, ProfileUpdateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('verify-email/', VerifyCodeView.as_view(), name='verify_email'),
    path('update-profile/', ProfileUpdateView.as_view(), name='update_profile'),
]
