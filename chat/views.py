from rest_framework import generics, permissions
from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer

class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]

class MessageListCreateView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        room_id = self.kwargs['room_id']
        return Message.objects.filter(room_id=room_id).order_by("timestamp")

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
