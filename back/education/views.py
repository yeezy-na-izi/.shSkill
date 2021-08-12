from django.shortcuts import render, redirect
from django.contrib.auth import login
from user.models import Account, Student
from user.forms import LoginUserForm, CreateUserForm
from education.forms import CreateCourse
from education.models import Course


def login_and_register(request):
    if 'login' in request.POST:
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
        return redirect(request.path)
    elif 'register' in request.POST:
        form = CreateUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            student = Student.objects.create(balance=0)
            user.student = student
            user.save()
            login(request, user)
        return redirect(request.path)


def home(request):
    if request.method == 'POST':
        login_and_register(request)
        context = {}
        return render(request, 'education/home.html')
    else:
        context = {'form': LoginUserForm}
        return render(request, 'education/home.html', context)


def unique_course(request, course_id):
    if request.method == 'POST':
        login_and_register(request)
    course = Course.objects.get(course_id=course_id)
    context = {'course': course}
    return render(request, 'education/unique_course.html', context)


def courses_list(request):
    if request.method == 'POST':
        login_and_register(request)
        if 'newCourse' in request.POST:
            form = CreateCourse(
                data=request.POST,
                files=request.FILES
            )
            form.save()
    form = CreateCourse()
    courses = Course.objects.all()
    l_courses = []
    for i in range(len(courses)):
        if i % 2 == 0:
            l_courses.append([])
        l_courses[-1].append(courses[i])
    context = {'courses': l_courses,
               'form': form}
    return render(request, 'education/courses.html', context)
