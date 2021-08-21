from django.shortcuts import render, redirect
from django.contrib import messages

from education.forms import CreateCourse, CreateLesson, CreateTask, CreateMaterialBlock
from education.models import Course, Lesson
from user.views import login_and_register


def home(request):
    if request.method == 'POST':
        login_and_register(request)
    context = {}
    return render(request, 'education/home/index.html', context)


def unique_course(request, course_id):
    course = Course.objects.get(course_id=course_id)
    if request.method == 'POST':
        login_and_register(request)
        if 'newLesson' in request.POST:
            form = CreateLesson(data=request.POST)
            if form.is_valid():
                x = form.save()
                course.lessons.add(x)
                course.save()
            else:
                messages.error(request, 'Что-то пошло не так')
    context = {'course': course}
    return render(request, 'education/unique_course/index.html', context)


def courses_list(request):
    if request.method == 'POST':
        login_and_register(request)
        if 'newCourse' in request.POST:
            form = CreateCourse(
                request.POST,
                request.FILES
            )
            print(1)
            if form.is_valid():
                form.save()
            else:
                messages.error(request, 'Что-то пошло не так')
        elif 'fixCourse' in request.POST:
            course = Course.objects.get(pk=request.POST['fixCourse'])
            course.title = request.POST['title']
            course.course_id = request.POST['course_id']
            course.description = request.POST['description']
            course.color = request.POST['color']
            if request.FILES:
                course.photo = request.FILES['photo']
            if 'show' in request.POST:
                course.show = True
            else:
                course.show = False
            course.save()
    form = CreateCourse()
    courses = Course.objects.order_by('pk')

    context = {'courses': courses,
               'form': form}
    return render(request, 'education/courses/index.html', context)


def tasks(request, course_id, pk):
    lesson = Lesson.objects.get(pk=pk)
    if request.method == 'POST':
        login_and_register(request)
        if 'newMaterialBlock' in request.POST:
            form = CreateMaterialBlock(data=request.POST, files=request.FILES)
            if form.is_valid():
                lesson.materials.blocks.add(form.save())
                lesson.save()
            else:
                for i in form.errors:
                    print(i)
                messages.error(request, 'Что-то пошло не так')
        elif 'newTask' in request.POST:
            form = CreateTask(data=request.POST)
            if form.is_valid():
                x = form.save()
                lesson.tasks.add(x)
                lesson.save()
            else:
                messages.error(request, 'Что-то пошло не так')
    context = {'lesson': lesson}
    return render(request, 'education/lesson/index.html', context)


def materials(request, course_id, pk):
    lesson = Lesson.objects.get(pk=pk)
    material = lesson.materials
    if request.method == 'POST':
        login_and_register(request),
    context = {'material': material}
    return render(request, 'education/material/index.html', context)
