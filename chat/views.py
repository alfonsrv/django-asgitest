from django.contrib.auth.models import User
from django.shortcuts import render


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})


def test(request):
    users = User.objects.all()
    return render(request, "chat/test.html", {'users': users})
