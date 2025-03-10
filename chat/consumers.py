import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
from django.contrib.auth import get_user_model

User = get_user_model()



class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f"chat_{self.room_id}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        sender_id = data['sender_id']
        text = data['text']

        user = await User.objects.get(id=sender_id)
        room = await Room.objects.get(id=self.room_id)

        message = await Message.objects.create(room=room, sender=user, text=text)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "sender": user.username,
                "text": text,
                "timestamp": str(message.timestamp),
            },
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))
