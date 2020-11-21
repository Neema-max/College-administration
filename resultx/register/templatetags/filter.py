from django import template
from ..models import teachers,subjects
register = template.Library()

@register.filter
def filter(value,arg):#value = teacher id #arg = sub id
    teacher = teachers.objects.filter(id= value).first()
    subj_t = teacher.subject.all()
    sub = subjects.objects.filter(id = arg).first()
    for x in subj_t:
        if x.s_id  == sub.s_id:
            return True
    return False