from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses_list, name='courses'),
    path('courses/<course_id>/', views.unique_course, name='unique_course'),
    path('courses/<course_id>/<slug>/', views.lesson_page, name='unique_course'),
    path('courses/<course_id>/<slug>/material/', views.materials, name='material'),
    path('courses/<course_id>/<slug>/<index>/', views.task, name='task')
]
