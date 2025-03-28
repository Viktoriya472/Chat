from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Users(models.Model):
    avatar = models.ImageField(upload_to="users_avatar/", blank=True, default="users_avatar/default.jpg")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Contacts(models.Model):
    name = models.CharField(max_length=150)
    phone_number = PhoneNumberField(unique=True, blank=False)
    avatar = models.ImageField(upload_to="users_avatar/", blank=True, default="users_avatar/default.jpg")
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
