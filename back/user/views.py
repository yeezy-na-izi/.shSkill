from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage

from user.forms import LoginUserForm, CreateUserForm
from user.utils import token_generator
from user.models import Account, Student
from education.models import Group

from user.models import Account
from user.utils import return_correct_phone


def login_and_register(request):
    if 'login' in request.POST:
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
        messages.success(request, 'Вы успешно вошли')
        return redirect(request.path)
    elif 'register' in request.POST:
        form = CreateUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            student = Student.objects.create(balance=0)
            user.student = student
            user.is_active = False
            user_id = urlsafe_base64_encode(force_bytes(user.username))
            domain = get_current_site(request).domain
            relative = reverse('activate', kwargs={'user_id': user_id, 'token': token_generator.make_token(user)})
            activate_url = f'http://{domain}{relative}'

            email_subject = 'Подтверждение почты'
            email_body = f'Привет, {user.username}, это активация аккаунта, перейди по ссылке чтобы ' \
                         f'верефицировать свой аккаунт\n{activate_url}'
            email = EmailMessage(email_subject, email_body, 'noreply@semycolon.com', [user.email], )
            try:
                email.send(fail_silently=False)
                messages.success(request, 'На почту пришло письмо, перейдите по ссылке и активруйте аккаунт')
            except:
                messages.error(request, 'Что-то пошло не так')
            user.save()
        return redirect(request.path)


def verification_email(request, user_id, token):
    if request.user.is_authenticated:
        messages.success(request, 'Вы уже авторизованны')
        return redirect(f'/profile/{request.user.username}')
    try:
        username = force_text(urlsafe_base64_decode(user_id))
        user = Account.objects.get(username=username)
        if token_generator.check_token(user, token) and not user.is_active:
            user.is_active = True
            user.save()
            messages.success(request, 'Аккаунт успешко активирован')
            return redirect('/')
        messages.error(request, 'Аккаунт по каким-то причинам не был активирован')
        return redirect('/')
    except:
        messages.error(request, 'Что-то пошло не так')
    return redirect('/')


def profile(request, username):
    user = Account.objects.get(username=username)
    try:
        student = user.student
        ended_courses_l = Group.objects.filter(users=student, ended=True)
        ended_courses = []
        for i in range(len(ended_courses_l)):
            if i % 2 == 0:
                ended_courses.append([])
            ended_courses[-1].append(ended_courses_l[i].course)
        in_progress_courses_l = Group.objects.filter(users=student, ended=False)
        in_progress_courses = []
        for i in range(len(in_progress_courses_l)):
            if i % 2 == 0:
                in_progress_courses.append([])
            in_progress_courses[-1].append(in_progress_courses_l[i].course)
    except:
        ended_courses = []
        in_progress_courses = []
    user.phone = return_correct_phone(user.phone)
    context = {
        'user': user,
        'ended': ended_courses,
        'not_ended': in_progress_courses
    }
    return render(request, 'user/profile.html', context)


def logout_page(request):
    messages.info(request, f'Вы вышли из аккаунта {request.user}')
    logout(request)
    return redirect('/')


def teachers(request):
    context = {}
    return render(request, 'user/teachers.html', context)
