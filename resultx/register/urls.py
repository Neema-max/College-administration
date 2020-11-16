from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('',views.getin, name='getin'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard/add_teacher/',views.add_teacher,name='add_teacher'),
    path('dashboard/add_admin/',views.add_admin,name='add_admin'),
    path('dashboard/add_course/',views.add_course,name='add_course'),
    path('dashboard/add_subject/',views.add_subject,name='add_subject'),
    path('dashboard/add_student/',views.add_student,name='add_student'),
    path('logout/',views.log_out,name='logout')
]