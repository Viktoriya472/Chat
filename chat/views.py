from chat.models import Contacts, Chat, Message
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from chat.forms import ContactForm, ChatForm
from django.urls import reverse_lazy
from django.db.models import Q


class ChatListView(LoginRequiredMixin, ListView):
    model = Chat
    template_name = 'chats/chat.html'
    context_object_name = 'chats'

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('q', '')
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        context['contacts'] = Contacts.objects.filter(
            Q(name__icontains=query) | Q(phone_number__icontains=query)
                                       ).distinct()
        return context


class Room(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'room.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        chat_name = self.kwargs['chat_name']
        # Изменить проверку доступа к страницам
        if Chat.objects.get(name=chat_name):
            context['chat_name'] = chat_name
        context['picture_chat'] = Chat.objects.filter(
            name=chat_name).values_list('picture', flat=True)
        return context


class CreateContact(LoginRequiredMixin, CreateView):
    model = Contacts
    template_name = 'contacts/create_contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('chat')


class CreateChat(LoginRequiredMixin, CreateView):
    models = Chat
    template_name = 'chats/create_chat.html'
    form_class = ChatForm
    success_url = reverse_lazy('chat')
