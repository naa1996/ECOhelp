from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     """
#     Абстрактный класс Пользователя
#     """
#     phone = models.CharField(max_length=12, verbose_name='Телефон')
#     points = models.IntegerField(verbose_name='Количество баллов')
#     role = models.CharField(max_length=20, verbose_name='Роль')
#     rating = models.IntegerField(verbose_name='Рейтинг')
#     code = models.IntegerField(verbose_name='Код')


class Status(models.Model):
    """
    Статус
    """
    status_name = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.status_name


class Task(models.Model):
    """
    Задания
    """
    name = models.CharField(max_length=100, verbose_name='Название')
    desc = models.CharField(max_length=500, verbose_name='Описание')
    cost = models.IntegerField(verbose_name='Стоимость')
    location = models.CharField(max_length=100, verbose_name='Местонахождение')
    photo = models.BinaryField(verbose_name='Фото')
    # user = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    # status = models.ForeignKey('Status', on_delete=models.DO_NOTHING)
    # id_executor = models.ForeignKey('User', on_delete=models.DO_NOTHING)