# Generated by Django 3.2.8 on 2021-11-09 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0018_alter_task_creator_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creator_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
    ]
