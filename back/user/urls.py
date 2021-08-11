from django.urls import path
from . import views

urlpatterns = [
    path('profile/<username>', views.profile, name='profile'),
    path('logout', views.logout_page, name='logout_page'),
]
