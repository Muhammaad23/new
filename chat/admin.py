from django.contrib import admin
from .models import ChatRoom, Message  # Room o'rniga ChatRoom

admin.site.register(ChatRoom)
admin.site.register(Message)
