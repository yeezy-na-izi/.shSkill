from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage

from user.models import Account, Student
from user.forms import LoginUserForm, CreateUserForm
from user.utils import token_generator

from education.forms import CreateCourse, CreateLesson
from education.models import Course, Lesson


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
            email.send(fail_silently=False)

            user.save()
        return redirect(request.path)


def home(request):
    if request.method == 'POST':
        login_and_register(request)
        context = {}
        return render(request, 'education/home/index.html')
    else:
        context = {'form': LoginUserForm}
        return render(request, 'education/home/index.html', context)


def unique_course(request, course_id):
    course = Course.objects.get(course_id=course_id)
    if request.method == 'POST':
        login_and_register(request)
        if 'newLesson' in request.POST:
            form = CreateLesson(data=request.POST)
            if form.is_valid():
                x = form.save()
                course.lessons.add(x)
                course.save()
            else:
                messages.error(request, 'Что-то пошло не так')
    context = {'course': course}
    return render(request, 'education/unique_course/index.html', context)


def courses_list(request):
    if request.method == 'POST':
        login_and_register(request)
        if 'newCourse' in request.POST:
            form = CreateCourse(
                data=request.POST,
                files=request.FILES
            )
            if form.is_valid():
                form.save()
            else:
                messages.error(request, 'Что-то пошло не так')
    form = CreateCourse()
    courses = Course.objects.all()
    l_courses = []
    for i in range(len(courses)):
        if i % 2 == 0:
            l_courses.append([])
        l_courses[-1].append(courses[i])
    context = {'courses': l_courses,
               'form': form}
    return render(request, 'education/courses/index.html', context)


def tasks(request, course_id, pk):
    lesson = Lesson.objects.get(pk=pk)
    context = {'lesson': lesson}
    return render(request, 'education/lesson/index.html', context)
