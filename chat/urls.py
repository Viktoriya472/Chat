from django.urls import path
from chat import views


urlpatterns = [
    path("", views.Chat.as_view(), name="chat"),
    path("<int:user_id>/", views.room, name="room"),
]
