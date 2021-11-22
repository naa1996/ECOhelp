# Generated by Django 3.2.8 on 2021-11-05 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0009_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12, verbose_name='Телефон')),
                ('points', models.IntegerField(verbose_name='Количество баллов')),
                ('role', models.CharField(max_length=20, verbose_name='Роль')),
                ('rating', models.IntegerField(verbose_name='Рейтинг')),
                ('code', models.CharField(max_length=256, verbose_name='Код')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
