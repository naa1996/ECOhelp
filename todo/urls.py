from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #роут страницы регистрации
    path('reg/', views.reg, name='reg'),
    #роут регистрации пользователя
    path('reg/createUser', views.createUser, name='createUser'),
    # path('reg/UReg', views.UReg, name='UReg'),
    # роут для отображения страницы
    path('', views.index),
]