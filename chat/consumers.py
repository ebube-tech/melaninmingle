# chat/consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from account.models import Account, Profile
from .models import Message
from groupchat.models import GroupMember, Room


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.sender = self.scope['user']
        # self.username = self.scope["url_route"]["kwargs"]["username"]
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        sender = text_data_json["sender"]
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message, 'sender' : sender}
        )

    # Receive message from room group
    async def chat_message(self, event):
        self.sender = self.scope['user']
        message = event["message"]
        # sender = await self.get_first_name()
        sender = event["sender"]
        print(event)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message, "sender": sender}))

    @database_sync_to_async
    def get_first_name(self):
        user = Profile.objects.get(user=self.sender)
        first_name = user.first_name 
        return first_name