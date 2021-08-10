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
        ended_courses = Group.objects.filter(users=student, ended=True)
        in_progress_courses = Group.objects.filter(users=student, ended=False)
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
