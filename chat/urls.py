from django.urls import path
from chat import views


urlpatterns = [
    path("", views.chat, name="chat"),
    path("<str:room_name>/", views.room, name="room"),
]
