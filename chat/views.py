# chat/views.py
from django.shortcuts import render
from django.contrib.auth import get_user_model


def user_list(request):
    User = get_user_model()
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request, "chat/user_list.html", context)


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})