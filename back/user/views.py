from django.shortcuts import render, redirect
from django.contrib.auth import logout
from user.models import Account


def myPage(request):
    context = {}
    return render(request, 'user/myPage.html', context)


def profile(request, username):
    user = Account.objects.get(username=username)
    context = {'user': user}
    return render(request, 'user/profile.html', context)


def logout_page(request):
    logout(request)
    return redirect('/')
