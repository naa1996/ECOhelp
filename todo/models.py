from django.db import models
# from django.conf import settings
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
    # photo = models.BinaryField(verbose_name='Фото')
    photo = models.ImageField(upload_to='media/', blank=False, verbose_name='Фото')
    achievement = models.CharField(max_length=500, verbose_name='Достижение')
    # status = models.CharField(max_length=100, verbose_name='Статус')
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, default=2, verbose_name='Статус')
    creator_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Создатель')
    # executor_user = models.OneToOneField(User, on_delete=models.DO_NOTHING, verbose_name='Исполнитель')


class Profile(models.Model):
    """
    Пользователь доп
    """
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Пользователь')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    points = models.IntegerField(verbose_name='Количество баллов')
    role = models.CharField(max_length=20, verbose_name='Роль')
    rating = models.IntegerField(verbose_name='Рейтинг')
    code = models.CharField(max_length=256, verbose_name='Код')


class TaskDone(models.Model):
    """
    Выполненное задание
    """
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Пользователь')
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING, verbose_name='Задание')
    photo = models.ImageField(upload_to='media/', blank=False, verbose_name='Фото')
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, default=2, verbose_name='Статус')