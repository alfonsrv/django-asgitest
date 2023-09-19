# chat/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path("test/", views.test, name="test"),
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
]
