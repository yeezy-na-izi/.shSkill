from django.contrib import admin
from .models import Task, Lesson, Course, Group, Date

admin.site.register(Task)
admin.site.register(Lesson)
admin.site.register(Course)
admin.site.register(Group)
admin.site.register(Date)
