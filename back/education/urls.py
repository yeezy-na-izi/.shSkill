from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses_list, name='courses'),
    path('courses/<course_id>/', views.unique_course, name='unique_course'),
    path('courses/<course_id>/<pk>/', views.tasks, name='unique_course'),
    path('courses/<course_id>/<pk>/material', views.materials, name='material')
]
