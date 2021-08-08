from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('1', views.test, name='test')
]
