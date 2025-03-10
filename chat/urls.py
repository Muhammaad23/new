from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChatRoomViewSet, MessageViewSet

# Router yaratish
router = DefaultRouter()
router.register(r'chatrooms', ChatRoomViewSet)  # /api/chatrooms/
router.register(r'messages', MessageViewSet)    # /api/messages/

urlpatterns = [
    path('api/', include(router.urls)),  # Barcha URL-larni avtomatik qo'shish
]
