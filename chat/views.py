from django.shortcuts import render
from chat.models import Chat, Message
from django.views.generic import ListView
from main.models import Contacts


class Chat(ListView):
    model = Chat
    template_name = "chat.html"
    context_object_name = "chats"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contacts.objects.all()
        return context


class Room(ListView):
    model = Message
    template_name = "room.html"

    def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            context['chat_name']= self.kwargs['chat_name']
            return context
