from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from .models import Status, Task, UserProfile
from django.contrib.auth.models import User


admin.site.register(Status)
admin.site.register(Task)


class UserInLine(admin.StackedInline):
    models = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


class UserAdmin(UserAdmin):
    inlines = (UserInLine,)


# Перерегистрируем модель User
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
