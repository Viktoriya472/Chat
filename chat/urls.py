from django.urls import path
from chat import views


urlpatterns = [
    path("", views.ChatListView.as_view(), name="chat"),
    path("create_contact/", views.CreateContact.as_view(),
         name="create_contact"),
    path("create_chat/", views.CreateChat.as_view(),
         name="create_chat"),
    path("<str:chat_name>/", views.Room.as_view(), name='room'),
]
