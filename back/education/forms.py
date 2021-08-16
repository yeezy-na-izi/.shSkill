from django import forms
from .models import Course, Lesson


class CreateCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title',
            'course_id',
            'description',
            'photo',
            'color'
        ]


class CreateLesson(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = [
            'title',
            'description',
            'price',
            'show'
        ]
