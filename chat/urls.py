# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.user_list, name="user_list"),
    path("<str:room_name>/", views.room, name="room"),
]