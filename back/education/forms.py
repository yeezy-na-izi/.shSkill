from django import forms
from .models import Course


class CreateCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'course_id',
                  'description', 'photo',
                  'color']