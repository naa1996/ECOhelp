# Generated by Django 3.2.8 on 2021-10-28 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0013_alter_userprofile_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='points',
            field=models.IntegerField(null=True, verbose_name='Количество баллов'),
        ),
    ]
