from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from .models import Status, Task
from django.contrib.auth.models import User


admin.site.register(Status)
admin.site.register(Task)
