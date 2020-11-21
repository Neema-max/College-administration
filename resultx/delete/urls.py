from django.urls import path , include
from . import views
urlpatterns = [
    path('student/',views.delete_student_home,name='delete_student_home'),
    path('teacher/',views.delete_teacher_home,name='delete_teacher_home'),
    path('subject/',views.delete_subject_home,name='delete_subject_home'),
    path('course/',views.delete_course_home,name='delete_course_home'),
    path('course/<int:id>/',views.delete_course, name='delete_course'),
    path('subject/<int:id>/',views.delete_subject, name='delete_subject'),
    path('student/<int:id>/',views.delete_student, name='delete_student'),
    path('teacher/<int:id>/',views.delete_teacher, name='delete_teacher'),
]