from django.shortcuts import render
from . import forms
from django.shortcuts import redirect
from .forms import UReg
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import User, UserProfile
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
            u = User.objects.filter(userprofile__points=0).all()
            s = User.objects.filter(userprofile__code="0000").all()
            v = User.objects.filter(userprofile__role="user").all()
            a = User.objects.filter(userprofile__rating=0000).all()
            vv = User.objects.filter(userprofile__role="admin").all()
            # ss = User.objects.filter(userprofile__).all()
            qq = User.objects
            vv = User._meta.fields
            print(u)
            print(s)
            print(v)
            print(a)
            # print(ss)
            print(vv)
            return redirect(auth)
        else:
            # print("Неверный пароль")
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


def user_form(request):
    #отображение информации/изменение
    # w = User.objects.get(id= int(request.POST['id_post']))
    # emails = request.POST['emailPR']
    # phone = request.POST['phonePR']
    # first_name = request.POST['first_namePR']
    # last_name = request.POST['last_name']
    # password = request.POST['passwordPR']
    # password2 = request.POST['password2PR']
    # id_post = request.POST['id_post']
    # print(id_post)
    # print(emails, phone, first_name, last_name, password, password2)
    # print(last_name)
    # ss = User.objects.filter(id = int(request.POST['id_post']))
    # id = request.POST['id_post']
    # print(id)
    if request.method == "POST":
        form = forms.UserProfile(request.POST)
        if request.POST['password'] == request.POST['password2']:
            print(User._meta._get_fields())
            print(request.POST['phone'])
            ss = User.objects.filter(id = int(request.POST['id_post']))
            vv = UserProfile._meta.fields
            print(vv)
            if ss:
                # if form.is_valid():
                User.objects.filter(id = int(request.POST['id_post'])).update(
                    # User.objects.update(
                    email=request.POST['email'],
                    # phone=request.POST['phone'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    password=request.POST['password'],
                )
                # sp = UserProfile.objects.filter(user = int(request.user.id))
                # if sp:
                #     UserProfile.objects.filter(user = int(request.user.id)).update(
                #         # UserProfile.objects.filter(user = int(request.user.id)).update(
                #         phone=request.POST['phone'],
                #     )
                #     vv = User.objects.filter(userprofile__user = " ").all()
                #     print(vv)

                messages.error(request, 'Информация успешно обновлена/изменена', extra_tags='safePR')
                    # s2s = User.objects.filter(userprofile__phone='').all()
                    # print(s2s)
                return redirect('user_form')
                # else:
                #     print('нет')
                #     messages.error(request, 'НЕТ', extra_tags='safePR')
                #     s2s = User.objects.filter(userprofile__phone='').all()
                #     s2r = User.objects.filter(userprofile__code='0000').all()
                #     print(s2s)
                #     print(s2r)
                #     return redirect('user_form')
            # else:
            #     messages.error(request, 'Не удалось обновить информацию', extra_tags='safePR')
            #     return redirect('user_form')
            else:
                messages.error(request, 'Не удалось', extra_tags='safePR')
                return redirect('user_form')
        else:
            messages.error(request, 'Пароли не совпали', extra_tags='safePR')
            return redirect('user_form')

    return redirect(user_setting)


def user_setting(request):
    #отображение страницы личной информации ползователя
    form = forms.UserProfile
    return render(request, 'user_setting.html', {
        'title': 'Личная информация',
        'user_form': form,
    })


def user_profile(request):
    #отображение страницы профиля
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