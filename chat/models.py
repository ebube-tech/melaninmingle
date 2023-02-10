from django.db import models
from django.conf import settings
from account.models import Account
# from chat.models import MessageGroup

Auth_User = settings.AUTH_USER_MODEL
# Create your models here.

class Message(models.Model):
    msg_sender = models.ForeignKey(Auth_User,  on_delete=models.CASCADE)
    conversation = models.ForeignKey('groupchat.Room', on_delete=models.CASCADE)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.msg_sender.email


# class Participants(models.Model):
#     msg_sender = models.ForeignKey(Auth_User,  on_delete=models.CASCADE)
#     conversation = models.ForeignKey('groupchat.Conversation', on_delete=models.CASCADE)    
