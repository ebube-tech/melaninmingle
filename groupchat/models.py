from django.db import models
from django.conf import settings
from account.models import Account

Auth_User = settings.AUTH_USER_MODEL

# Create your models here.

class Room(models.Model):
    group_name = models.CharField(max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.group_name


class GroupMember(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ManyToManyField(Auth_User)

    joined_date = models.DateTimeField(auto_now_add=True)
    left_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.email


