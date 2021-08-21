from django import template

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
