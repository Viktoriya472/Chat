from django.db import models
from main.models import Users, Contacts


class Chat(models.Model):
    name = models.CharField(max_length=130)
    contacts = models.ManyToManyField(Contacts, related_name='chat_contacts')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Чат"
        verbose_name_plural = "Чаты"


class Message(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.name}: {self.text}'

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"