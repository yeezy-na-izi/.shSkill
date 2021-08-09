from django.shortcuts import render


def myPage(request):
    context = {}
    return render(request, 'user/myPage.html', context)
