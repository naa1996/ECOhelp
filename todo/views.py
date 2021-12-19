from django.shortcuts import render
from . import forms
from django.shortcuts import redirect
from .forms import UReg
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import User, Profile, Task, Status, TaskDone
from os.path import  basename
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required


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


def logout(request):
    request.session.clear()
    return redirect(auth)


def auth(request):
    # отображение страницы авторизации
    if not request.user.is_authenticated:
        return render(request, 'auth.html', {
            'title': 'Авторизация',
        })
    else:
        return redirect(user_profile)


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
    if request.user.is_authenticated:
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
    else:
        return redirect(auth)


def id_task(request):
    id_user = request.POST['id_user']
    id_task = request.POST['id_task']
    # id_task_done = request.POST['id_task_done']
    print(id_user)
    print(id_task)
    # print(id_task_done)
    request.session['id_task'] = id_task
    request.session['id_user'] = id_user
    # request.session['id_task_done'] = id_task_done
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
        #изменение статуса задания при проверке всех заданий
        if prov:
            if not admin:
                #+++
                #если задание  НЕ от разработчиков
                #статус - выполнено/доработать
                print('статус1')
                status2 = request.POST['status2']
                print(status2)
                Task.objects.filter(id=id_task).update(
                    status = status,
                )
                TaskDone.objects.filter(id=id_task_done).update(
                    status = status,
                )
                return redirect(user_profile)
            # else:
            #         #если задание  НЕ от разработчиков
            #         #статус - доработать
            #         print('статус2')
            #         status = request.POST['status']
            #         print(status)
            #         TaskDone.objects.filter(id=id_task_done).update(
            #             status = status,
            #         )
            #         Task.objects.filter(id=id_task).update(
            #             status =
            #         )
            #         return redirect(user_profile)
            else:
                id_status = int(request.POST['status'])
                if id_status != 4:
                    #если задание от разработчиков выполнено
                    print('статус3')
                    status2 = request.POST['status2']
                    print('l2', status2)
                    status = request.POST['status']
                    print('k', status)
                    Task.objects.filter(id=id_task).update(
                        status = status2,
                    )
                    TaskDone.objects.filter(id=id_task_done).update(
                        status = status,
                    )
                    return redirect(user_profile)
                else:
                    #если задание от разработчиков отправлено на доработку
                    print('статус11')
                    status2 = request.POST['status2']
                    print(status)
                    Task.objects.filter(id=id_task).update(
                        status = status2,
                    )
                    TaskDone.objects.filter(id=id_task_done).update(
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
    if request.user.is_authenticated:
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
        user_task_complete = TaskDone.objects.filter(user=id_user).all()
        # user_task_complete = TaskDone.objects.filter(user=id_user).order_by('-id')[:2]
        print('user_task_complete', user_task_complete)
        print(user_task_dones)
        admin = User.objects.filter(username='admin')
        admin_2 = User.objects.get(username='admin').username
        print('admin', admin)
        print('admin', admin_2)
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
            if admin:
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
    else:
        return redirect(auth)


def rating(request):
    if request.user.is_authenticated:
        # отображение страницы рейтинга пользователей
        id_user = request.session['id_user']
        print('id_user', id_user)
        user_rating = Profile.objects.filter(user=id_user).all()
        return render(request, 'rating.html', {
            'title': 'Рейтинг',
            'user_rating': user_rating,
        })
    else:
        return redirect(rating)


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
        # new_user = '' это что ? :D
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
    if request.user.is_authenticated:
        d = Task.objects.filter(creator_user=4).all()
        return render(request, 'tasks.html', {
            'title': 'Задания',
            'task_photo': d
        })
    else:
        return redirect(auth)


def task_watch(request):
    # отображение задания на странице задания Task
    #под вопросом????
    redirect('task')


def task(request):
    # отображение страницы задания
    if request.user.is_authenticated:
        id_task = request.session['id_task']
        print('id_task', id_task)
        id_user = request.session['id_user']
        print('id_user', id_user)
        # task_table = Task.objects.get(id=id_task)
        # task_table = Task.objects.get(id=id_task)
        task_table = Task.objects.filter(id=id_task).all()
        task_photo = Task.objects.filter(id=id_task).all()
        print('task_table', task_table)
        print('PHOTO: ', task_photo[0].photo)
        request.session['id_task'] = id_task
        request.session['id_user'] = id_user
        return render(request, 'task.html', {
            'title': 'Задание',
            'task': task_table,
            'task_photo': task_photo,
            # 'media_url': settings.MEDIA_URL,
        })
    else:
        return redirect(auth)


def task_form_save(request):
    # сохранение ответа на задания
        id_task = request.session['id_task']
        print('id_task', id_task)
        id_user = request.session['id_user']
        print('id_user', id_user)

        return redirect('task_accept')


def task_accept_user(request):
    # отправка фотографии о выполнении
    if request.method == 'POST':
        #проверка загрузки
        if request.FILES.get('image'):
            # image = request.FILES['image']
            # print(image)
            # exit()
            #проверка загрузки фотографии
            if 'image' in request.FILES['image'].content_type:
                foto = request.FILES['image']
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
                status0 = Status.objects.get(id=request.POST['status0'])
                status_int = int(task)
                print(status_int, status_int)
                print(status)
                print(status0)
                if status_int < 13:
                    print(11)
                    TaskDone.objects.create(
                        user = authorized_user,
                        task = task0,
                        photo = foto,
                        status = status,
                    )
                    print('ok')
                    print('Запись добавлена')
                    messages.error(request, 'Ответ принят', extra_tags='safeTA')
                    Task.objects.filter(id=task).update(
                        status = status0,
                    )
                    print('Status ok')

                    #сохранение фотографии
                    fs = FileSystemStorage()
                    fs.save(foto.name, foto)

                    messages.error(request, 'Задание успешно добавлено', extra_tags='safeCT')
                    messages.error(request, 'Статус изменен', extra_tags='safeTA')
                    return redirect('task_accept')
                else:
                    print(22)
                    TaskDone.objects.create(
                        user = authorized_user,
                        task = task0,
                        photo = foto,
                        status = status,
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
            else:
                print('Загружена не фотография!')
                messages.error(request, 'Загружена не фотография', extra_tags='safeTA')
                return redirect('task_accept')
        else:
            print('Фотография не загружена!')
            messages.error(request, 'Неверный тип файла', extra_tags='safeTA')
            return redirect('task_accept')
    print('exit')
    return redirect('task_accept')


def task_accept(request):
    # отображение страницы описания задания от разработчика
    if request.user.is_authenticated:
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
    else:
        return redirect(auth)


def u_create_task(request):
    # добавление нового задания пользователем
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        location = request.POST['location']
        cost = request.POST['radio']
        #проверка загрузки
        if request.FILES.get('image'):
            # image = request.FILES['image']
            # print(image)
            # exit()
            #проверка загрузки фотографии
            if 'image' in request.FILES['image'].content_type:
                image = request.FILES['image']
                # up_file = request.FILES['image']
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
                # request.session['id_status'] = status
                # user = authenticate(username=nss, password=password)
                if ss:
                    if not f:
                        if(name != desc):
                            if 'image' in request.FILES['image'].content_type:
                                # exit()
                                # des = ' '.join(id)
                                # print(des)
                                # status = 'Ожидание'
                                # achievement = 'Молодец! Ты помог природе! Ей стало по-легче'
                                Task.objects.create(
                                     name=name,
                                     desc=desc,
                                     cost=cost,
                                     location=location,
                                     photo=image,
                                     achievement=achievement,
                                     status=status,
                                     creator_user=authorized_user,
                                )

                                print('Задание успешно добавлено')
                                fs = FileSystemStorage()
                                fs.save(image.name, image)
                                messages.error(request, 'Задание успешно добавлено', extra_tags='safeCT')
                                return redirect('user_create_task')
                            else:
                                print('Загружена не фотография')
                                messages.error(request, 'Загружена не фотография', extra_tags='safeCT')
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
                print('Загружена не фотография!')
                messages.error(request, 'Загружена не фотография', extra_tags='safeCT')
                return redirect('user_create_task')
        else:
            print('Фотография не загружена!')
            messages.error(request, 'Неверный тип файла', extra_tags='safeCT')
            return redirect('user_create_task')

    else:
        return redirect('user_create_task')


def user_create_task(request):
    # отображение страницы создания задания пользователем
    if request.user.is_authenticated:
        return render(request, 'user_create_task.html', {
            'title': 'Добавить задание',
        })
    else:
        return redirect(auth)


def user_task_accept(request):
    # отображение страницы описания задания от пользователя
    if request.user.is_authenticated:
        return render(request, 'user_task_accept.html', {
            'title': 'Страница описания задания'
        })
    else:
        return redirect(auth)


def user_task_complete(request):
    # отображение выполнения задания от пользователя
    if request.user.is_authenticated:
        id_task = request.POST['id_task']
        print('id_t', id_task)
        id_user = request.POST['id_user']
        print('id_u', id_user)
        id_task_done = request.POST['id_task_done']
        print('id_task_done', id_task_done)
        task = Task.objects.filter(id=id_task).all()
        task_done = TaskDone.objects.filter(id=id_task_done).all()
        print('task', task)
        return render(request, 'user_task_complete.html', {
                'title': 'Статус задания',
                'task_complete': task,
                'task_done_status': task_done,

        })
    else:
        return redirect(auth)


def user_task_completed(request):
    # отображение страницу откликов пользователя
    if request.user.is_authenticated:
        id_task = request.session['id_task']
        print('id_tasks', id_task)
        id_user = request.session['id_user']
        print('id_users', id_user)
        user_task_completed = TaskDone.objects.filter(user=id_user).all()
        return render(request, 'user_task_completed.html', {
            'title': 'Мои отклики',
            'user_task_completed': user_task_completed,

        })
    else:
        return redirect(auth)


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
    if request.user.is_authenticated:
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
                #id_task_done = request.POST['id_task_done']
                print('id_task_done', id_user)
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
    else:
        return redirect(auth)


def user_task_photo(request):
    # отображение странциы  о выполнения задания
    if request.user.is_authenticated:
        return render(request, 'user_task_photo.html', {
            'title': 'Страница о выполнении задания'
        })
    else:
        return redirect(auth)