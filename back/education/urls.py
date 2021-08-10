from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('coursesfaq', views.coursesFAQ, name='CoursesFAQ'),
    path('courses', views.courses_list, name='courses'),
    path('courses/<courses_id>', views.coursesFAQ, name='course')
]
