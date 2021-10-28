from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save


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


class UserProfile(models.Model):
    """
    Дополнительные поля Пользователя
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь', unique=True)
    phone = models.CharField(max_length=12, verbose_name='Телефон', unique=True)
    points = models.IntegerField(verbose_name='Количество баллов', default='0000000', editable=False)
    role = models.CharField(max_length=20, verbose_name='Роль', default='user', editable=False)
    rating = models.IntegerField(verbose_name='Рейтинг', default='0000000', editable=False)
    code = models.CharField(max_length=256, verbose_name='Код', default='0000', editable=False)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)

    def __unicode__(self):
        return self.user_id

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
