from django import template
from .models import PaidLesson
register = template.Library()


@register.filter(name='split_to')
def split1(value, key):
    if len(value) >= key:
        x = value
        while '<' in value[len(value) - len(x):key] and '>' in x:
            z = value.index('>')
            key += z - value.index('<')
            x = x[:z + 1]
        return value[:key] + '...'
    return value


@register.filter(name='split_from')
def split2(value, key):
    if len(value) <= key:
        return value[key:]
    return ''


@register.filter(name='my_sort')
def split1(my_object, key):
    return my_object.order_by(key)


@register.filter(name='join_with')
def join_with(my_object, key: str):
    return key.join(my_object.split(key)[:-2])


@register.filter(name='file_split')
def file_split(my_object, key: str):
    x = str(my_object)
    return key.join(x.split(key)[1:])


@register.filter(name='getPercents')
def PercentsProgress(solved, allTasks):
    try:
        return int(int(solved) / int(allTasks) * 100)
    except (ValueError, ZeroDivisionError):
        return None


@register.filter(name='getSolvedTasks')
def getSolvedTask(user, lesson):
    try:
        return len(PaidLesson.objects.get(user=user.student, lesson=lesson).solved_tasks.all())
    except PaidLesson.DoesNotExist:
        return 0