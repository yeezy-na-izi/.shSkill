from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages

from education.models import Group

from user.models import Account
from user.utils import return_correct_phone


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
