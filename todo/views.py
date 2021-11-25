from django.shortcuts import render
from . import forms
from django.shortcuts import redirect
from .forms import UReg
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import User, Profile, Task, Status, TaskDone


def index(request):
    # отображение главной страницы
    return render(request, 'index.html', {
        'title': 'Главная страница',
    })


def loginn(request):
    # авторизация
    email = request.POST['email']
    password = request.POST['password']
    m = User.objects.filter(email=email).exists()
    if m:
        n = User.objects.get(email=email).username
        id_user = User.objects.get(username=n).id
        user = authenticate(username=n, password=password)
        if user is not None:
            # print("Правильно")
            # messages.error(request, 'Правильно', extra_tags='safe')
            login(request, user)

            request.session['id_user'] = id_user
            # u = User.objects.filter(userprofile__points=0).all()
            # s = User.objects.filter(userprofile__code="0000").all()
            # v = User.objects.filter(userprofile__role="user").all()
            # a = User.objects.filter(userprofile__rating=0000).all()
            # vv = User.objects.filter(userprofile__role="admin").all()
            # vv = User.objects.filter(userprofile__phone='').all()
            # qq = User.objects
            # vv = User._meta.fields
            ms = Profile.objects.filter(user=user).exists()
            if not ms:
                phone = '89997778855'
                points = 000
                role = 'user'
                rating = 000
                code = 0000
                Profile.objects.create(
                    user=user,
                    phone=phone,
                    points=points,
                    role=role,
                    rating=rating,
                    code=code,
                )
                return redirect(user_profile)
            else:
                request.session['id_user'] = id_user
                print('Уже существует')
                return redirect(user_profile)
            # return redirect(create_profile)
        else:
            # print("Неверный пароль")
            messages.error(request, 'Неверный пароль', extra_tags='safe')
            return redirect(auth)
    else:
        # print("Неверная почта")
        messages.error(request, 'Неверная почта', extra_tags='safe')
        return redirect(auth)


# def logout(request):
#     print('ss')
#     # return redirect(auth)
#     return render(request, 'auth.html', {'title': 'Выход'})


def auth(request):
    # отображение страницы авторизации
    return render(request, 'auth.html', {
        'title': 'Авторизация',
    })


def recovery_password(request):
    # восстановление пароля
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
    # отображение страницы восстановления
    return render(request, 'recovery_pass.html', {
        'title': 'Восстановление',
    })


def user_form(request):
    # отображение информации/изменение
    # w = User.objects.get(id= int(request.POST['id_post']))
    # ss = User.objects.filter(id = int(request.POST['id_post']))
    # phone = request.POST['phone']
    # print(request.POST['phone'])
    if request.method == "POST":
        if request.POST['password'] == request.POST['password2']:
            print(User._meta._get_fields())
            print(Profile._meta._get_fields())
            ss = User.objects.filter(id = int(request.POST['id_post']))
            if ss:
                User.objects.filter(id = int(request.POST['id_post'])).update(
                    email=request.POST['email'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    password=request.POST['password'],
                    )


                email = request.POST['email']
                m = User.objects.filter(email=email).exists()
                print(m)
                n = User.objects.get(email=email).id
                print(n)
                if m:
                    s = Profile.objects.filter(user=n).exists()
                    v = Profile.objects.filter(user=n).values('phone')
                    print(s)
                    print(v)
                    if s:
                        phone = request.POST['phone']
                        print(phone)
                        if len(phone) == 11:
                            if phone.isdigit:
                                # ms = Profile.objects.filter(user=n).exists()
                                Profile.objects.filter(user=n).update(
                                    phone = request.POST['phone']
                                )
                                messages.error(request, 'Информация успешно обновлена/изменена', extra_tags='safePR')
                                return redirect('user_form')
                            else:
                                messages.error(request, 'Не удалось обновить информацию. Неверный формат записи телефона', extra_tags='safePR')
                                return redirect('user_form')

                        else:
                            messages.error(request, 'Не удалось обновить информацию. Неверный формат номера', extra_tags='safePR')
                            return redirect('user_form')
                    else:
                        messages.error(request, 'Не удалось обновить информацию', extra_tags='safePR')
                        return redirect('user_form')
                else:
                    messages.error(request, 'Не удалось обновить информацию', extra_tags='safePR')
                    return redirect('user_form')

                # messages.error(request, 'Информация успешно обновлена/изменена', extra_tags='safePR')
                #
                # return redirect('user_form')

            else:
                messages.error(request, 'Не удалось обновить информацию', extra_tags='safePR')
                return redirect('user_form')
        else:
            messages.error(request, 'Пароли не совпали', extra_tags='safePR')
            return redirect('user_form')

    return redirect(user_setting)


def user_setting(request):
    # отображение страницы личной информации ползователя
    id_user = request.session['id_user']
    print('id_user', id_user)
    form = forms.UserProfile
    user_profile_phone = Profile.objects.filter(user=id_user).all()
    return render(request, 'user_setting.html', {
        'title': 'Личная информация',
        'user_form': form,
        'user_profile_phone': user_profile_phone,
    })


def id_task(request):
    id_user = request.POST['id_user']
    id_task = request.POST['id_task']
    print(id_user)
    print(id_task)
    request.session['id_task'] = id_task
    request.session['id_user'] = id_user
    return redirect(user_task_completed)


def adoption_task(request):
    # изменение статуса выполненного задания
    if request.method == "POST":
        status = request.POST['status']
        print(status)
        # status_o = request.POST['status_o']
        # print(status_o)
        id_task = request.POST['id_task']
        print(id_task)
        #отправка id статуса
        request.session['id_task'] = id_task
        username = request.POST['username']
        user = User.objects.get(username=username).id
        print('username', username)
        print(user)
        cost = int(Task.objects.get(id=request.POST['id_task']).cost)
        print('стоимость', cost)
        authorized_user = User.objects.get(id=user)
        print('хорошо')
        #добавление баллов
        profile = Profile.objects.get(user=authorized_user)
        profile.points += cost
        profile.save()
        id_task_done = request.POST['id_task_done']
        print('id_task_done', id_task_done)
        #изменение статуса
        admin = Task.objects.filter(id=id_task).filter(creator_user=1)
        prov = TaskDone.objects.filter(task=id_task).filter(user=user)
        print(admin)
        if prov:
            if not admin:
                #если задание  НЕ от разработчиков
                print('статус1')
                status2 = request.POST['status']
                print(status2)
                Task.objects.filter(id=id_task).update(
                    status = status,
                )
                return redirect(user_profile)

            elif(int(request.POST['status']) == 4):
                    print('статус2')
                    status = request.POST['status']
                    print(status)
                    Task.objects.filter(id=id_task).update(
                        status = status,
                    )
                    return redirect(user_profile)
            else:
                #если задание от разработчиков выполнено
                print('статус3')
                status = request.POST['status2']
                print(status)
                Task.objects.filter(id=id_task).update(
                    status = status,
                )
                return redirect(user_profile)
        return redirect(user_profile)


def delete_adoption_task(request):
    # удаление записи о выполнении задания
    if request.method == "POST":
        id_del = request.POST['id_del']
        print('id_del', id_del)
        TaskDone.objects.filter(id=id_del).delete()
    return redirect(user_profile)


def user_profile(request):
    # отображение страницы профиля
    id_user = request.session['id_user']
    print('id_user', id_user)
    request.session['id_user'] = id_user
    # id_task = request.POST['id_task']
    # print(id_task)
    #отправка id статуса
    # request.session['id_task'] = id_task
    #отображение количества баллов пользователя
    user_profile_points = Profile.objects.filter(user=id_user).all()
    #отображение достижений пользователя
    # user_achievement = TaskDone.objects.filter(user=id_user).all()
    user_achievement = TaskDone.objects.filter(user=id_user).order_by('-id')[:2]
    print('Все задания Task', user_achievement)
    user = TaskDone.objects.filter(user=id_user)
    # print('Задания на которые откликнулся пользователь TaskDone', user)
    #отображение таблицы с заданиями
    user_task_dones = TaskDone.objects.all()
    # user_task_complete = TaskDone.objects.filter(user=id_user).all()
    user_task_complete = TaskDone.objects.filter(user=id_user).order_by('-id')[:2]
    print('user_task_complete', user_task_complete)
    print(user_task_dones)
    if user:
        print(11)
        return render(request, 'user_profile.html', {
            'title': 'Профиль',
            'user_profile_points': user_profile_points,
            'user_achievement': user_achievement,
            'user_task_dones': user_task_dones,
            'user_task_complete': user_task_complete,
        })
    else:
        print('Вы не откликались на задания')
        messages.error(request, 'Вы не откликались на задания. Достижений пока нет', extra_tags='UP')
        return render(request, 'user_profile.html', {
            'title': 'Профиль',
            'user_profile_points': user_profile_points,
            'user_achievement': user_achievement,
            # 'user_task_complete': user_task_complete,
            # 'user_task_dones': user_task_dones,
        })




def createUser(request):
    # регистрация
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


def task_form(request):
    # передача данных из страницы Tasks (задания от разработчиков)
    # print(1)
    id_user = request.POST['id_user']
    print('id_user', id_user)
    id_task = request.POST['id_task']
    print('id_task', id_task)
    request.session['id_task'] = id_task
    request.session['id_user'] = id_user
    return redirect('task')


def tasks(request):
    # отображение страницы заданий
    # form = forms.TaskPhoto()
    d = Task.objects.filter(creator_user=1).all()
    return render(request, 'tasks.html', {
        'title': 'Задания',
        'task_photo': d
    })


def task_watch(request):
    # отображение задания на странице задания Task
    #под вопросом????
    redirect('task')


def task(request):
    # отображение страницы задания
    id_task = request.session['id_task']
    print('id_task', id_task)
    id_user = request.session['id_user']
    print('id_user', id_user)
    # task_table = Task.objects.get(id=id_task)
    # task_table = Task.objects.get(id=id_task)
    task_table = Task.objects.filter(id=id_task)
    print('task_table', task_table)
    request.session['id_task'] = id_task
    request.session['id_user'] = id_user
    return render(request, 'task.html', {
        'title': 'Задание',
        'task': task_table,
    })


def task_form_save(request):
    # сохранение ответа на задания
        id_task = request.session['id_task']
        print('id_task', id_task)
        id_user = request.session['id_user']
        print('id_user', id_user)

        return redirect('task_accept')


def task_accept_user(request):
    # отображение страницы описания задания от разработчика
    #     id_task = request.session['id_task']
    #     print('id_task', id_task)
    #     id_user = request.session['id_user']
        # print('id_user', id_user)
    if request.method == 'POST':
        foto = request.POST['foto']
        print(foto)
        user = request.session['id_user']
        print(user)
        task = request.session['id_task']
        print(task)
        status = request.POST['status']
        print(status)
        print('ok')
        authorized_user = User.objects.get(id=user)
        task0 = Task.objects.get(id=task)
        status = Status.objects.get(id=request.POST['status'])
        print(request.POST['status'])
        TaskDone.objects.create(
            user = authorized_user,
            task = task0,
            photo = foto,
        )
        print('ok')
        print('Запись добавлена')
        messages.error(request, 'Ответ принят', extra_tags='safeTA')
        Task.objects.filter(id=task).update(
            status = status,
        )
        print('Status ok')

        messages.error(request, 'Статус изменен', extra_tags='safeTA')
        return redirect('task_accept')
    print('exit')
    return redirect('task_accept')


def task_accept(request):
    # отображение страницы описания задания от разработчика
    id_task = request.session['id_task']
    print('id_task', id_task)
    id_user = request.session['id_user']
    print('id_user', id_user)
    task_table_accept = Task.objects.filter(id=id_task)
    print('task_table', task_table_accept)
    #передача на страницу task_accept_user
    request.session['id_task'] = id_task
    request.session['id_user'] = id_user
    return render(request, 'task_accept.html', {
        'title': 'Описание задания разработчика',
        'task_accept': task_table_accept,
    })


def u_create_task(request):
    # добавление нового задания пользователем
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        location = request.POST['location']
        cost = request.POST['radio']
        foto = request.POST['foto']
        id = request.POST['id_post']
        email = request.POST['email']
        achievement = request.POST['achievement']
        # password = request.POST['password']
        # status = request.POST['
        id_status = int(request.POST['id_post'])
        #отправка данных статуса
        request.session['id_status'] = id_status
        print(name)
        print(desc)
        print(location)
        print(cost)
        print(id)
        print(email)
        print(achievement)
        # print(password)
        # print(status)
        f = Task.objects.filter(name=name)
        ss = User.objects.filter(id = int(request.POST['id_post']))
        print(ss)
        n = User.objects.get(email=email)
        print(n)
        nss = User.objects.get(email=email).username
        print('user', nss)
        password = User.objects.get(email=email).password
        print('pass', password)
        authorized_user = User.objects.get(id=id)
        status = Status.objects.get(id=request.POST['status'])
        request.session['id_status'] = status
        # user = authenticate(username=nss, password=password)
        if ss:
            if not f:
                if(name != desc):
                    des = ' '.join(id)
                    print(des)
                    # status = 'Ожидание'
                    # achievement = 'Молодец! Ты помог природе! Ей стало по-легче'
                    Task.objects.create(
                         name=name,
                         desc=desc,
                         cost=cost,
                         location=location,
                         photo=foto,
                         achievement=achievement,
                         status=status,
                         creator_user=authorized_user,

                    )
                    print('Задание успешно добавлено')
                    messages.error(request, 'Задание успешно добавлено', extra_tags='safeCT')
                    return redirect('user_create_task')
                else:
                    print('Описание такое же как название! Опишите по подробнее')
                    messages.error(request, 'Описание такое же как название! Опишите по подробнее', extra_tags='safeCT')
                    return redirect('user_create_task')
            else:
                print('Задание с таким названием уже существует')
                messages.error(request, 'Задание с таким названием уже существует', extra_tags='safeCT')
                return redirect('user_create_task')
        else:
            print('З33')
            messages.error(request, 'З33', extra_tags='safeCT')
            return redirect('user_create_task')
    else:
        return redirect(user_create_task)


def user_create_task(request):
    # отображение страницы создания задания пользователем
    return render(request, 'user_create_task.html', {
        'title': 'Добавить задание',
    })


def user_task_accept(request):
    # отображение страницы описания задания от пользователя
    return render(request, 'user_task_accept.html', {
        'title': 'Страница описания задания'
    })


def user_task_complete(request):
    # отображение выполнения задания от пользователя
    id_task = request.POST['id_task']
    print('id_t', id_task)
    id_user = request.POST['id_user']
    print('id_u', id_user)
    task = Task.objects.filter(id=id_task).all()
    print('task', task)
    task_status = Task.objects.get(id=id_task).status
    print('task_status', task_status)
    task_s_admin = Task.objects.filter(id=id_task).filter(status='2')
    print('task_s_admin', task_s_admin)
    if TaskDone.objects.filter(user = id_user).filter(task=id_task):
        return render(request, 'user_task_complete.html', {
            'title': 'Статус задания',
            'task_complete': task,
        })
    else:
        print(2)
        return render(request, 'user_task_complete.html', {
            'title': 'Статус задания',
            'task_complete': task,

        })


def user_task_completed(request):
    # отображение страницу откликов пользователя
    id_task = request.session['id_task']
    print('id_tasks', id_task)
    id_user = request.session['id_user']
    print('id_users', id_user)
    user_task_completed = TaskDone.objects.filter(user=id_user).all()
    return render(request, 'user_task_completed.html', {
        'title': 'Мои отклики',
        'user_task_completed': user_task_completed,

    })


def user_task_form(request):
    id_user = request.POST['id_user']
    print('id_user', id_user)
    id_task = request.POST['id_task']
    print('id_task', id_task)
    request.session['id_task'] = id_task
    request.session['id_user'] = id_user
    return redirect('task')


def user_task_list(request):
    # отображение страницы списка заданий пользователя
    #приём id пользователя
    id_user = request.session['id_user']
    print('id_user', id_user)
    # id_status = request.session['id_status']
    # print('id_status', id_status)
    u = User.objects.filter(username = 'admin')
    us = User.objects.get(username = 'admin').id
    print('sdh', u)
    print('hds', us)
    # if not Task.objects.filter(status=2):
    if id_user == 1:
            print(12)
            user_task_table = Task.objects.exclude(creator_user = id_user).filter(status=2).all()
            request.session['id_user'] = id_user
            return render(request, 'user_task_list.html', {
                    'title': 'Список задний от пользователей',
                    'user_task_list': user_task_table,
            })
    else:
            print(21)
            user_task_table = Task.objects.exclude(creator_user= us).filter(status=2).all()
            request.session['id_user'] = id_user
            return render(request, 'user_task_list.html', {
                    'title': 'Список задний от пользователей',
                    'user_task_list': user_task_table,
            })
    # else:
    #     print('Заданий нет')
    #     messages.error(request, 'Заданий нет', extra_tags='safeUL')
    #     return render(request, 'user_task_list.html', {
    #         'title': 'Список задний от пользователей',
    #
    #     })


def user_task_photo(request):
    # отображение странциы  о выполнения задания
    return render(request, 'user_task_photo.html', {
        'title': 'Страница о выполнении задания'
    })