from django.shortcuts import render, redirect
from django.contrib.auth import login
from user.models import Account
from user.forms import LoginUserForm
from education.models import Course


def home(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            form = LoginUserForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
            return redirect(request.path)
        context = {}
        return render(request, 'education/home.html')
    else:
        context = {'form': LoginUserForm}
        return render(request, 'education/home.html', context)


def coursesFAQ(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'education/coursesfaq.html', context)
