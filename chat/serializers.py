# chat/serializers.py
from rest_framework import serializers
from .models import ChatRoom, Message  # To'g'ri model nomidan foydalaning

class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
