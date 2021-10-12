from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from .models import Status, Task

admin.site.register(Status)
admin.site.register(Task)
# admin.site.register(User, UserAdmin)


