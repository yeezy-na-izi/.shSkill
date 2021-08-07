from django.shortcuts import render


def first_try(request):
    context = {}
    return render(request, 'user/first_try.html', context)
