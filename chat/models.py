from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Users(models.Model):
    avatar = models.ImageField(upload_to="users_avatar/",
                               blank=True, default="users_avatar/default.jpg")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.ForeignKey("Contacts", on_delete=models.CASCADE)
    chat = models.ForeignKey("Chat", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Contacts(models.Model):
    name = models.CharField(max_length=150)
    phone_number = PhoneNumberField(unique=True, blank=False)
    avatar = models.ImageField(upload_to="users_avatar/",
                               blank=True, default="users_avatar/default.jpg")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Chat(models.Model):
    name = models.CharField(max_length=130)
    picture = models.ImageField(upload_to="chat_picture/", blank=True,
                                default="chat_picture/default.jpg")
    contact = models.ManyToManyField(Contacts)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Чат"
        verbose_name_plural = "Чаты"


class Message(models.Model):
    text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    # у сообщения должен быть или контакт или пользователь
    # user = models.ForeignKey(Users, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.user.username}: {self.text}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
