from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses', views.courses_list, name='courses'),
    path('courses/<courses_id>', views.unique_course, name='unique_course')
]
