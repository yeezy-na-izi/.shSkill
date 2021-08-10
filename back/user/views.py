from django.shortcuts import render, redirect
from django.contrib.auth import logout
from user.models import Account
from education.models import Group


def myPage(request):
    context = {}
    return render(request, 'user/myPage.html', context)


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
    context = {
        'user': user,
        'ended': ended_courses,
        'not_ended': in_progress_courses
    }
    return render(request, 'user/profile.html', context)


def logout_page(request):
    logout(request)
    return redirect('/')
