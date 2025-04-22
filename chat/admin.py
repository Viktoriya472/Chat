from django.contrib import admin
from chat.models import Users, Contacts, Chat, Message


admin.site.register(Users)
admin.site.register(Contacts)
admin.site.register(Chat)
admin.site.register(Message)
