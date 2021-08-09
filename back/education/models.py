from django.db import models
from user.models import Student, Teacher


class Task(models.Model):
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    title = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Условие задачи')

    def __str__(self):
        return self.title


class Lesson(models.Model):
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    title = models.CharField(verbose_name='Название', max_length=100)
    tasks = models.ManyToManyField(verbose_name='Задачи', to=Task, blank=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    title = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание')
    lessons = models.ManyToManyField(verbose_name='Уроки', to=Lesson)
    price = models.FloatField(verbose_name='Цена')

    def __str__(self):
        return self.title


class Group(models.Model):
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    users = models.ManyToManyField(verbose_name='Ученики', to=Student)
    teacher = models.ForeignKey(verbose_name='Учитель', to=Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(verbose_name='Курс', to=Course, on_delete=models.CASCADE)
    chat = models.URLField(verbose_name='Ссылка на чат')
    title = models.CharField(verbose_name='Заголовок', max_length=100)

    def __str__(self):
        return self.title


class Date(models.Model):
    class Meta:
        verbose_name = 'Дата'
        verbose_name_plural = 'Даты'

    group = models.ForeignKey(verbose_name='Группа', to=Group, on_delete=models.CASCADE)
    date_time = models.DateTimeField(verbose_name='Время и дата')
    description = models.TextField(verbose_name='Описание')
    lesson_link = models.URLField(verbose_name='Ссылка на подключение')
    lesson = models.ForeignKey(verbose_name='Урок', to=Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date_time} {self.group}"
