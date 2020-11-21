from django import template
from register.models import courses,c_teacher_sub
register = template.Library()

@register.filter
def co_sub(value,arg):#value = course id #arg = c_teacher id
    c = courses.objects.get(id = int(value))
    for x in c.c_teacher.all() :
        if x.id == int(arg):
            return True
    return False