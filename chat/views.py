# chat/views.py
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db.models import Q
from account.models import Profile
from groupchat.models import Room, GroupMember


def user_list(request):
    users = Profile.objects.all().exclude(user__email=request.user)

    context = {
        'users':users,
    }
    return render(request, "chat/user_list.html", context)


def room(request, username):
    User = get_user_model()
    current_user = User.objects.get(email=request.user)
    other_user = User.objects.get(profile__username=username)
    current_user_username = current_user.profile.username
    first_name = current_user.profile.first_name
    
    print(type(first_name))
    new_room_name = (current_user_username + username).replace('-','_')
    prev_room_name = (username + current_user_username).replace('-','_')

    try:
        obj = Room.objects.get(group_name=prev_room_name)
        room_name = obj.group_name
    except:
        try:
            room = Room.create(new_room_name)
            group_member1 = GroupMember.create(room, current_user)
            group_member2 = GroupMember.create(room, other_user)
            room_name =  room.group_name
        except:
            room_name = new_room_name

    return render(request, "chat/room.html", {"room_name": room_name, 'first_name': first_name})
