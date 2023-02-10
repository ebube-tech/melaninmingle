from django.db import models
from django.conf import settings
from account.models import Account

Auth_User = settings.AUTH_USER_MODEL

# Create your models here.

class Room(models.Model):
    group_name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.group_name


# class GroupMemberManger(models.Manager):
#     def by_user(self, user):
#         qlookup = Q(first=user) | Q(second=user)
#         qlookup2 = Q(first=user) & Q(second=user)
#         qs = self.get_queryset().filter(qlookup).exclude(qlookup2).distinct()
#         return qs

#     def get_or_new(self, user, other_username): # get_or_create
#         username = user.username
#         if username == other_username:
#             return None
#         qlookup1 = Q(first__username=username) & Q(second__username=other_username)
#         qlookup2 = Q(first__username=other_username) & Q(second__username=username)
#         qs = self.get_queryset().filter(qlookup1 | qlookup2).distinct()
#         if qs.count() == 1:
#             return qs.first(), False
#         elif qs.count() > 1:
#             return qs.order_by('timestamp').first(), False
#         else:
#             Klass = user.__class__
#             user2 = Klass.objects.get(username=other_username)
#             if user != user2:
#                 obj = self.model(
#                         first=user, 
#                         second=user2
#                     )
#                 obj.save()
#                 return obj, True
#             return None, False




class GroupMember(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ManyToManyField(Auth_User)

    joined_date = models.DateTimeField(auto_now_add=True)
    left_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.email


