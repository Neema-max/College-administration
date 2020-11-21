from django.shortcuts import render,redirect,reverse
from register.models import student,teachers,profile,subjects,courses,c_teacher_sub
# Create your views here.
def delete_student_home(request):
    params={
        'student' : student.objects.all(),
    }
    return render(request,'delete/delete_student_home.html',params)
def delete_teacher_home(request):
    params={
        'teacher' : teachers.objects.all(),
        'subjects' : subjects.objects.all(),
    }
    return render(request,'delete/delete_teacher_home.html',params)
def delete_subject_home(request):
    params={
        'subjects' : subjects.objects.all(),
    }
    return render(request,'delete/delete_subject_home.html',params)
def delete_course_home(request):
    params={
        'courses' : courses.objects.all(),
        'subjects' : subjects.objects.all(),
        'c_sub': c_teacher_sub.objects.all(),
    }
    return render(request,'delete/delete_course_home.html',params)
def delete_course(request,id):
    c = courses.objects.get(id = id)
    c.delete()
    return redirect(reverse('delete_course_home'))
def delete_subject(request,id):
    sub  = subjects.objects.get(id=id)
    sub.delete()
    return redirect(reverse('delete_subject_home'))
def delete_student(request,id):
    s = student.objects.get(id=id)
    s.profile.user.delete()
    s.profile.delete()
    s.delete()
    return redirect(reverse('delete_student_home'))
def delete_teacher(request,id):
    t = teachers.objects.get(id=id)
    t.profile.user.delete()
    t.delete()
    return redirect(reverse('delete_teacher_home'))