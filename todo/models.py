from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


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
    status = models.ForeignKey('Status', on_delete=models.DO_NOTHING, default='2', verbose_name='Статус')
    creator_user = models.OneToOneField(User, on_delete=models.DO_NOTHING, verbose_name='Создател')
    # executor_user = models.OneToOneField(User, on_delete=models.DO_NOTHING, verbose_name='Исполнитель')