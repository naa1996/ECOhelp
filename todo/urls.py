from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    # роут для отображения страницы - Регистрация
    path('reg', views.reg, name='reg'),
    #роут регистрации пользователя
    path(r'createUser', views.createUser, name='createUser'),
    # path('reg/UReg', views.UReg, name='UReg'),
    # роут для отображения страницы - Авторизация
    path('auth/', views.auth, name='auth'),
    # роут для авторизации
    path(r'^accounts/login/', views.loginn, name='login'),
    # роут восстановления пароля
    path('recovery_password', views.recovery_password, name='recovery_password'),
    # роут для отображения страницы - Восстановление пароля
    path('recovery', views.recovery_pass, name='recovery_pass'),
    # роут для отображения страницы - Профиль
    path('profile', views.user_profile, name='user_profile'),
    # роут для отображения страницы - Главная
    path('', views.index, name='index'),
    # path('index1', views.index1, name='index1'),
]
