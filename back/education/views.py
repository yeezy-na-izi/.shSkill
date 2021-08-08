from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'education/home.html')


def test(request):
    context = {}
    return render(request, 'education/home2.html')
