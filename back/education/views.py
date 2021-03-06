from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404

from education.forms import CreateCourse, CreateLesson, CreateTask, CreateMaterialBlock, CreateExamples
from education.models import Course, Lesson, Group, PaidLesson, randomString
from user.views import login_and_register


def home(request):
    if request.method == 'POST':
        login_and_register(request)
        return redirect(request.path)
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
        return redirect(request.path)
    context = {'course': course}
    if request.user.student:
        paidLessons = []
        for lesson in PaidLesson.objects.filter(user=request.user.student):
            paidLessons.append(lesson.lesson)
        context['paidLessons'] = paidLessons
    return render(request, 'education/unique_course/index.html', context)


def courses_list(request):
    if request.method == 'POST':
        login_and_register(request)
        if 'newCourse' in request.POST:
            form = CreateCourse(
                request.POST,
                request.FILES
            )
            form.slug = randomString()
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
        elif 'removeCourse' in request.POST:
            course = Course.objects.get(pk=request.POST['removeCourse'])
            course.delete()
        return redirect(request.path)
    form = CreateCourse()
    courses = Course.objects.order_by('pk')

    context = {'courses': courses,
               'form': form}
    return render(request, 'education/courses/index.html', context)


def lesson_page(request, course_id, slug):
    try:
        lesson = Course.objects.get(course_id=course_id).lessons.all().get(slug=slug)
    except Lesson.DoesNotExist:
        raise Http404('Страницы не существует')
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
                lesson.lesson_page.add(x)
                lesson.save()
            else:
                messages.error(request, 'Что-то пошло не так')
        return redirect(request.path)
    context = {'lesson': lesson}
    if not request.user.teacher:
        try:
            paid_lesson = PaidLesson.objects.get(lesson=lesson, user=request.user.student)
            context = {'lesson': lesson, 'paid_lesson': paid_lesson}
        except PaidLesson.DoesNotExist:
            messages.error(request, 'Вы еще не оплатили урок')
            return redirect('/'.join(request.path.split('/')[:-2]))
    return render(request, 'education/lesson/index.html', context)


def pay_for_lesson(request, course_id, slug):
    lesson = Course.objects.get(course_id=course_id).lessons.all().get(slug=slug)
    if request.user.student:
        if request.user.student.balance >= lesson.price:
            obj, create = PaidLesson.objects.get_or_create(lesson=lesson, user=request.user.student)
            if create:
                request.user.student.balance -= lesson.price
                request.user.student.save()
                messages.success(request, 'Вы успешно оплатили урок')
            else:
                messages.info(request, 'Вы уже оплачивали данный урок')
        else:
            messages.error(request, 'У вас недостаточно средств')
            return redirect('/'.join(request.path.split('/')[:-3]))
    return redirect('/'.join(request.path.split('/')[:-2]))


def materials(request, course_id, slug):
    try:
        lesson = Course.objects.get(course_id=course_id).lessons.all().get(slug=slug)
        material = lesson.materials
        if request.method == 'POST':
            login_and_register(request),
        context = {'material': material}
        return render(request, 'education/material/index.html', context)
    except Lesson.DoesNotExist:
        raise Http404('Страницы не существует')


def task(request, course_id, slug, index):
    try:
        lesson = Course.objects.get(course_id=course_id).lessons.all().get(slug=slug)
        unique_task = list(lesson.tasks.order_by('pk'))[int(index) - 1]
        if request.method == 'POST':
            login_and_register(request)
            if 'newExample' in request.POST:
                form = CreateExamples(data=request.POST)
                if form.is_valid():
                    x = form.save()
                    unique_task.examples.add(x)
                    unique_task.save()
                else:
                    messages.error(request, 'Что-то пошло не так')
            return redirect(request.path)
        context = {'task': unique_task}
        return render(request, 'education/task/index.html', context)
    except Lesson.DoesNotExist:
        raise Http404('Страницы не существует')
