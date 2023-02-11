# chat/views.py
from django.shortcuts import render
from django.contrib.auth import get_user_model
from account.models import Profile


def user_list(request):
    users = Profile.objects.all().exclude(user__email=request.user)

    context = {
        'users':users,
    }
    return render(request, "chat/user_list.html", context)


def room(request, username):
    User = get_user_model()
    current_user_username = User.objects.get(email=request.user).profile.username
    print(current_user_username)
    username = username.replace('-','_')
    room_name = 'v'
    return render(request, "chat/room.html", {"username": username})