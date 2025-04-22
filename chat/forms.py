from django.forms import ModelForm
from chat.models import Contacts, Chat
from django import forms


class ContactForm(ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'phone_number']


class ChatForm(ModelForm):
    class Meta:
        model = Chat
        fields = ['name', 'picture', 'contact']
        widgets = {
            'contact': forms.CheckboxSelectMultiple()
        }
