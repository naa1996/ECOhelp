from django.shortcuts import render
from . import models, forms
from django.shortcuts import redirect
from .models import User
from .forms import UReg
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# from .models import UserProfile


def index(request):
    return render(request, 'index.html', {
        'title': 'Главная страница',
    })


def index1(request):
    return render(request, 'index1.html', {
        'title': '123123',
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
                                messages.error(request, 'Не удалось завести пользователя', extra_tags='safe')
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
    #отображение страницы регистрации
    user_form = UReg()
    return render(request, 'reg.html', {
        'title': 'Регистрация',
        'create_user': user_form,
    })