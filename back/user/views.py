from django.shortcuts import render


def first_try(request):
    context = {}
    return render(request, 'extends/index.html', context)
