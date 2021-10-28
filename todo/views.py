from django.shortcuts import render
from . import forms
from django.shortcuts import redirect
from .forms import UReg
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import User
from django.db.models import Q


def index(request):
    #отображение главной страницы
    return render(request, 'index.html', {
        'title': 'Главная страница',
    })


def loginn(request):
    #авторизация
    email = request.POST['email']
    password = request.POST['password']
    m = User.objects.filter(email=email).exists()
    if m:
        n = User.objects.get(email=email).username
        user = authenticate(username=n, password=password)
        if user is not None:
            # print("Правильно")
            # messages.error(request, 'Правильно', extra_tags='safe')
            login(request, user)
            return redirect(auth)
        else:
            # print("Неверный пароль")
            print("Неверный пароль")
            messages.error(request, 'Неверный пароль', extra_tags='safe')
            return redirect(auth)
    else:
        # print("Неверная почта")
        messages.error(request, 'Неверная почта', extra_tags='safe')
        return redirect(auth)


def auth(request):
    #отображение страницы авторизации
    return render(request, 'auth.html', {
        'title': 'Авторизация',
    })


def recovery_password(request):
    #восстановление пароля
    emails = request.POST['emailP']
    print(emails)
    m = User.objects.filter(email=emails).exists()
    if m:
        print(m)

        messages.error(request, 'Почта верна', extra_tags='safe1')
        return redirect(recovery_pass)
    else:
        messages.error(request, 'Неверная почта', extra_tags='safe1')
        return redirect(recovery_pass)


def recovery_pass(request):
    #отображение страницы восстановления
    return render(request, 'recovery_pass.html', {
        'title': 'Восстановление',
    })


def user_profile(request):
    #отображение страницы авторизации
    return render(request, 'user_profile.html', {
        'title': 'Профиль',
    })


def createUser(request):
    #регистрация
    if request.method == 'POST':
        print(request.POST)
        user_reg_form = forms.UReg(request.POST)
        password2 = request.POST['password2']
        password1 = request.POST['password1']
        username1 = request.POST['username']
        first_name1 = request.POST['first_name']
        last_name1 = request.POST['last_name']
        email1 = request.POST['email']
        # print(username1)
        # print(first_name1)
        # print(last_name1)
        # print(email1)
        # print(password1)
        # print(password2)
        f = User.objects.filter(username=username1)
        ff = User.objects.filter(email=email1)
        # new_user = ''
        if not f:
            if not ff:
                if password1 == password2:
                    # print(models.User._meta._get_fields())
                    if not password1.isdigit():
                        if len(password1) >= 8:
                            if user_reg_form.is_valid():
                                # print('3')
                                new_user = user_reg_form.save(commit=False)
                                # print('3')
                                new_user.set_password(user_reg_form.cleaned_data['password1'])
                                # print('3')
                                new_user.save()
                                messages.error(request, 'Успешно зарегестрирован', extra_tags='safe')
                                return redirect('reg')
                            else:
                                # print(user_reg_form.errors)
                                messages.error(request, 'Не удалось зарегистрировать пользователя', extra_tags='safe')
                                # return HttpResponse(user_reg_form.errors)
                                return redirect('reg')
                        else:
                            messages.error(request, 'Пароль слишком короткий', extra_tags='safe')
                            return redirect('reg')
                    else:
                        messages.error(request, 'Пароль слишком легкий - содержит только цифры', extra_tags='safe')
                        return redirect('reg')

                else:
                    messages.error(request, 'Не заристрирован. Пароли не совпадают', extra_tags='safe')
                    return redirect('reg')
            else:
                messages.error(request, 'Не заристрирован. Пользователь с такой почтой уже существует', extra_tags='safe')
                return redirect('reg')
        else:
            messages.error(request, 'Не заристрирован. Пользователь с таким логином уже существует', extra_tags='safe')
            return redirect('reg')
    # else:
    #     messages.error(request, 'Не отправлен', extra_tags='safe')
    #     return redirect('reg')


def reg(request):
    # отображение страницы регистрации
    user_form = UReg()
    return render(request, 'reg.html', {
        'title': 'Регистрация',
        'create_user': user_form,
    })
