# Generated by Django 3.2.8 on 2021-11-09 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0020_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.DO_NOTHING, to='todo.status', verbose_name='Статус'),
        ),
    ]
