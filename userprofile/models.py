from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    Абстрактный класс Пользователя
    """
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, verbose_name='Пользователь')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    points = models.IntegerField(verbose_name='Количество баллов')
    role = models.CharField(max_length=20, verbose_name='Роль')
    rating = models.IntegerField(verbose_name='Рейтинг')
    code = models.IntegerField(verbose_name='Код')

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
