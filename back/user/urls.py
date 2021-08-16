from django.urls import path
from . import views

urlpatterns = [
    path('profile/<username>', views.profile, name='profile'),
    path('teachers', views.teachers, name='teachers'),
    path('logout', views.logout_page, name='logout_page'),
    path('activate/<user_id>/<token>', views.verification_email, name='activate'),
]
