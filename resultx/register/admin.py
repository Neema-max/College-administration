from django.contrib import admin
from .models import teachers,subjects,courses,student,profile,administrator,c_teacher_sub
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User
admin.site.register(c_teacher_sub)
admin.site.register(administrator)
admin.site.register(profile)
admin.site.register(teachers)
admin.site.register(subjects)
admin.site.register(courses)
admin.site.register(student)