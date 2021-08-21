from django import forms
from .models import Course, Lesson, Task, MaterialBlocks


class CreateCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title',
            'course_id',
            'description',
            'photo',
            'color',
            'show'
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


class CreateTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'color',

        ]


class CreateMaterialBlock(forms.ModelForm):
    class Meta:
        model = MaterialBlocks
        fields = [
            'title',
            'block',
            'color',
        ]
