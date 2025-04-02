from django.urls import path
from chat import views


urlpatterns = [
    path("", views.ChatListView.as_view(), name="chat"),
    path("<str:chat_name>/", views.Room.as_view(), name='room'),
]
