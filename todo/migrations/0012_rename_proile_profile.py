# Generated by Django 3.2.8 on 2021-11-05 15:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0011_rename_userp_proile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Proile',
            new_name='Profile',
        ),
    ]
