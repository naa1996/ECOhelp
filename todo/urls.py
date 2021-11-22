from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    # роут для отображения страницы - Регистрация
    path('reg', views.reg, name='reg'),
    #роут регистрации пользователя
    path(r'createUser', views.createUser, name='createUser'),
    # роут для отображения страницы - Авторизация
    path('auth/', views.auth, name='auth'),
    # роут для авторизации
    path(r'^accounts/login/', views.loginn, name='login'),
    # роут для выхода
    # path(r'^accounts/logout/$', views.logout, name='logout'),
    # роут восстановления пароля
    path('recovery_password', views.recovery_password, name='recovery_password'),
    # роут для отображения страницы - Восстановление пароля
    path('recovery', views.recovery_pass, name='recovery_pass'),
    # роут для отображения страницы - Информация о пользователе
    path('user_setting', views.user_setting, name='user_setting'),
    # роут для изменения данных о пользователе
    path('user_form', views.user_form, name='user_form'),
    # роут для изменения статуса выполненного задания
    path('adoption_task', views.adoption_task, name='adoption_task'),
    # роут для удаления записи о выполненном задании
    path('delete_adoption_task', views.delete_adoption_task, name='delete_adoption_task'),
    # роут для отображения страницы - Профиль
    path('profile', views.user_profile, name='user_profile'),
    # роут для отображения заданий от разработчиков
    path('task_form', views.task_form, name='task_form'),
    # роут для отображения страницы - Задания
    path('tasks', views.tasks, name='tasks'),
    # роут для отображения страницы - Задание
    path('task', views.task, name='task'),
    # роут для отображения страницы
    path('task_accept', views.task_accept, name='task_accept'),
    # роут для отправки фотографии о выполнении задания
    path('task_accept_user', views.task_accept_user, name='task_accept_user'),
    # роут для отображения страницы
    path('user_create_task', views.user_create_task, name='user_create_task'),
    # роут для добавления задания пользователем
    path('u_create_task', views.u_create_task, name='u_create_task'),
    # роут для отображения страницы
    path('user_task_accept', views.user_task_accept, name='user_task_accept'),
    # роут для отображения страницы
    path('user_task_complete', views.user_task_complete, name='user_task_complete'),
    # роут для отображения страницы
    path('user_task_completed', views.user_task_completed, name='user_task_completed'),
    # роут для перехода к просмотру задания пользователей
    path('user_task_form', views.user_task_form, name='user_task_form'),
    # роут для отображения страницы
    path('user_task_list', views.user_task_list, name='user_task_list'),
    # роут для отображения страницы
    path('user_task_photo', views.user_task_photo, name='user_task_photo'),

    # роут для отображения страницы - Главная
    path('', views.index, name='index'),
    # path('index1', views.index1, name='index1'),
]
