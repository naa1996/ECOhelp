# Generated by Django 3.2.8 on 2021-11-05 14:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0010_userp'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserP',
            new_name='Proile',
        ),
    ]
