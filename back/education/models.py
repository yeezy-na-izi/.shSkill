from django.db import models
from user.models import Student, Teacher


class MaterialBlocks(models.Model):
    class Meta:
        verbose_name = 'Блок материала'
        verbose_name_plural = 'Блоки материала'

    colours = (
        ('1', 'Голубой'),
        ('2', 'Розовый'),
        ('3', 'Фиолетовый'),
        ('4', 'Зеленый'),
        ('5', 'Розово-фиолетовый'),

    )
    icons = (
        ('bolt', 'Молния'),
        ('apple-alt', 'Яблоко'),
        ('balance-scale-left', 'Весы'),
        ('brain', 'Мозг'),
        ('check', 'Галочка'),
        ('cloud', 'Облако'),
        ('compass', 'Компас'),
        ('dev', 'dev'),
        ('git', 'git'),
        ('lemon', 'Лимон'),
    )
    title = models.CharField(max_length=256)
    block = models.FileField(verbose_name='Информация блока', upload_to='templates/education/material_sections')
    color = models.CharField(max_length=1, choices=colours)
    icon = models.CharField(max_length=32, choices=icons, default='bolt')


class Material(models.Model):
    class Meta:
        verbose_name = 'Материал урока'
        verbose_name_plural = 'Материалы урока'

    title = models.CharField(verbose_name='Название', max_length=64)
    blocks = models.ManyToManyField(verbose_name='Блоки', to=MaterialBlocks, blank=True)
    annotations = models.TextField(verbose_name='Аннотация', blank=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    colors = (
        ('#4169E1', 'Легкий уровень'),
        ('#ffaf00', 'Средний уровень'),
        ('#bb02ff', 'Сложный уровень'),
    )
    title = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Условие задачи')
    color = models.CharField(verbose_name='Цвет', choices=colors, max_length=7)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    title = models.CharField(verbose_name='Название', max_length=100)
    materials = models.ForeignKey(verbose_name='Материал', to=Material, blank=True, on_delete=models.CASCADE, null=True)
    tasks = models.ManyToManyField(verbose_name='Задачи', to=Task, blank=True)
    description = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена', default=1000)
    show = models.BooleanField(verbose_name='Показать на странице', default=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    colors = (
        ('primary', 'Синий'),
        ('secondary', 'Фиолетовый'),
        ('success', 'Зеленый'),
        ('danger', 'Красный'),
        ('warning', 'Желтый'),
        ('info', 'Голубой'),
        ('light', 'Прозрачный',),
        ('dark', 'Черный'),

    )
    title = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание')
    lessons = models.ManyToManyField(verbose_name='Уроки', to=Lesson, blank=True)
    color = models.CharField(verbose_name='Цвет', max_length=16, choices=colors, default='primary')
    course_id = models.CharField(verbose_name='Курс линк', max_length=100, unique=True)
    photo = models.ImageField(verbose_name='Фото',
                              upload_to='static/education/course', blank=True)
    show = models.BooleanField(verbose_name='Показать на странице')

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
    ended = models.BooleanField(verbose_name='Закончена', default=False)

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
