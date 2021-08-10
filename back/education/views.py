from django.shortcuts import render, redirect
from django.contrib.auth import login
from user.models import Account
from user.forms import LoginUserForm, CreateUserForm
from education.models import Course


def home(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            form = LoginUserForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
            return redirect(request.path)
        elif 'register' in request.POST:
            form = CreateUserForm(data=request.POST)
            if form.is_valid():
                user = form.save()
                user.save()
                login(request, user)
            return redirect(request.path)
        context = {}
        return render(request, 'education/home.html')
    else:
        context = {'form': LoginUserForm}
        return render(request, 'education/home.html', context)


def test(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'education/home2.html', context)
