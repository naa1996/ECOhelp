# Generated by Django 3.2.8 on 2021-10-28 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0018_alter_userprofile_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='code',
            field=models.IntegerField(default='0000', editable=False, max_length=256, verbose_name='Код'),
        ),
    ]
