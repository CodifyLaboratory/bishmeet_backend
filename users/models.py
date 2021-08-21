from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

GENDER_CHOICES = (
    ('others', 'Другое'),
    ('male', 'Мужской'),
    ('female', 'Женский')
)


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    age = models.CharField(verbose_name='Возраст', max_length=20)
    gender = models.CharField(verbose_name='Пол', max_length=20, choices=GENDER_CHOICES)
    avatar = models.ImageField(verbose_name='Фото', upload_to='user_pictures/')
    email = models.EmailField(verbose_name='Почта', max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name='Дата/время регистрации',
                                       auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Последний вход',
                                      auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
