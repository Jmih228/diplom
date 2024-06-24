from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    phone_number = models.CharField(max_length=12, verbose_name='Телефон')
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name='Город')
    invite_code = models.CharField(max_length=6, null=True, blank=True, verbose_name='invite code')
    auth_code = models.CharField(max_length=4, null=True, blank=True, verbose_name='Код авторизации')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class InviteCode(models.Model):

    value = models.CharField(max_length=6, verbose_name='Значение invite code')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Владелец инвайт кода')

    class Meta:
        verbose_name = 'Invite code'
        verbose_name_plural = 'Invite codes'

    def __str__(self):
        return self.value
