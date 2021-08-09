from django.urls import path
from . import views

urlpatterns = [
    # path('', views.first_try, name='FirstTry'),
    path('Perelman', views.myPage, name='MyPage')
]
