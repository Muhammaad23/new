from rest_framework import viewsets
from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-timestamp')
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]