from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from apps.users.managers import UserManager
from utils.user_phone_number_regex import phone_regex


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(verbose_name='Имя', max_length=128)
    last_name = models.CharField(verbose_name='Фамилия', max_length=128)
    phone_number = models.CharField(verbose_name='Номер телефона',
                                    validators=[phone_regex],
                                    max_length=20, unique=True)
    is_active = models.BooleanField(verbose_name='Активный', default=True)
    is_staff = models.BooleanField(verbose_name='Сотрудник', default=False)
    date_joined = models.DateTimeField(verbose_name='Зарегестрирован',
                                       default=timezone.now)

    USERNAME_FIELD = 'phone_number'

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.phone_number}'
