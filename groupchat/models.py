from django.db import models
from django.conf import settings
from account.models import Account

Auth_User = settings.AUTH_USER_MODEL

# Create your models here.

class Room(models.Model):
    group_name = models.CharField(max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def create(cls, group_name):
        # room = cls(group_name=group_name)
        room = cls.objects.create(group_name=group_name)
        return room

    def __str__(self) -> str:
        return self.group_name


class GroupMember(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(Auth_User, on_delete=models.CASCADE)

    joined_date = models.DateTimeField(auto_now_add=True)
    left_date = models.DateTimeField(auto_now=True)

    @classmethod
    def create(cls, room, user):
        # group_member = cls(room=room, user=user)
        group_member = cls.objects.create(room=room, user=user)
        return group_member

    def __str__(self) -> str:
        return self.user.email


