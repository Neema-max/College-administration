from django.shortcuts import render,reverse,redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password ,is_password_usable
from .models import student,teachers,administrator,profile,subjects
import re 
 #Create your views here.




def add_subject(request):
    if request.user.is_authenticated:
        user = request.user
        pro = profile.objects.filter(user=user).first()
        if int(pro.lev) == 3:
            if request.method =="POST":
                name = request.POST['name']
                name = name.strip()
                code =request.POST['code']
                code = code.strip()     
                if subjects.objects.filter(s_id=code):
                    data = {
                        'result' : 'error',
                        'message': 'subject code take'
                    }
                    return JsonResponse(data)
                elif subjects.objects.filter(name = name):
                    data = {
                        'result' : 'error',
                        'message': 'subject name take'
                    }
                    return JsonResponse(data)
                elif ' ' in code :
                    data = {
                        'result' : 'error',
                        'message': 'subject code cannot contain blank space'
                    }
                    return JsonResponse(data)
                else :
                    s = subjects(name=name,s_id=code)
                    s.save()
                    data={
                        'result' : 'success',
                    }
                    return JsonResponse(data)
            return render(request,'add_subject.html')
    return redirect(reverse('dashboard'))
v_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def check(email):  
    if(re.search(v_email,email)):  
        return True  
          
    else:  
        return False

def add_teacher(request):
    if request.user.is_authenticated:
        user = request.user
        pro = profile.objects.filter(user=user).first()
        sub = subjects.objects.all()
        params = {
            'subject' : sub,
        }
        if not sub and int(pro.lev) == 3:
            return redirect(reverse('add_subject'))
        if int(pro.lev) == 3:
            if request.method =="POST":
                fname = request.POST['firstname']
                fname= fname.strip()
                lname = request.POST['lastname']
                lname = lname.strip()
                email = request.POST['email']
                email = email.strip()
                username = request.POST['username']
                username =  username.strip()
                p1 =request.POST['p1']
                p2 = request.POST['p2']
                subId = request.POST.get('subjects')
                lev = request.POST['profile']
                regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')     
                if  User.objects.filter(username = username):
                    data={
                        'result' : 'error',
                        'message' : 'username taken',
                    }
                    return JsonResponse(data)
                elif ' ' in username:
                    data={
                        'result' : 'error',
                        'message' : 'username cannot contain blank space',
                    } 
                    return JsonResponse(data)
                elif p1 != p2:
                    data={
                        'result' :'error',
                        'message' : 'password mismatch',
                    }
                    return JsonResponse(data)
                elif len(p1)<8:
                    data={
                        'result' : 'error',
                        'message' : 'length of password must be 8 character'
                    }
                elif p1.isnumeric():
                    data={
                        'result' :'error',
                        'message' : 'password cannot be entierly numeric',
                    }
                    return JsonResponse(data)
                elif  regex.search(p1) is None: 
                    data={
                        'result':'error',
                        'message': 'Password must contain special character',
                    }
                    return JsonResponse(data)
                elif not check(email):
                    data={
                        'result':'error',
                        'message': 'Invalid email',
                    }
                    return JsonResponse(data)
                elif lname == '':
                    data={
                        'result':'error',
                        'message': 'Last name cannot be blank',
                    }
                    return JsonResponse(data)  
                elif fname == '':
                    data={
                        'result':'error',
                        'message': 'First name cannot be blank',
                    }
                    return JsonResponse(data)             
                else :
                    password = make_password(p1)
                    if is_password_usable(password):
                        r = User(username= username,password = password,first_name=fname,last_name=lname,email=email)
                        r.save()
                        x = profile(user= r,lev = int(lev))
                        x.save()
                        data = {
                            'result' : 'success',
                        }
                        return JsonResponse(data)
            return render(request,'add_teacher.html',params)
    return redirect(reverse('dashboard'))

def add_course(request):
    if request.user.is_authenticated:
        user = request.user
        pro = profile.objects.filter(user=user).first()
        if int(pro.lev) == 3:
            if request.method =="POST":
                username = request.POST['username']
                username = username.strip()
                p1 =request.POST['p1']
                p2 = request.POST['p2']
                lev = request.POST['profile']
                regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')  
                #print(username)   
                if  User.objects.filter(username = username):
                    data={
                        'result' : 'error',
                        'message' : 'username taken',
                    }
                    return JsonResponse(data)
                elif p1 != p2:
                    data={
                        'result' :'error',
                        'message' : 'password mismatch',
                    }
                    return JsonResponse(data)
                elif len(p1)<8:
                    data={
                        'result' : 'error',
                        'message' : 'length of password must be 8 character'
                    }
                elif p1.isnumeric():
                    data={
                        'result' :'error',
                        'message' : 'password cannot be entierly numeric',
                    }
                    return JsonResponse(data)
                elif  regex.search(p1) is None: 
                    data={
                        'result':'error',
                        'message': 'Password must contain special character',
                    }
                    return JsonResponse(data)
                else :
                    password = make_password(p1)
                    if is_password_usable(password):
                        r = User(username= username,password = password)
                        r.save()
                        x = profile(user= r,lev = int(lev))
                        x.save()
                        data = {
                            'result' : 'success',
                        }
                        return JsonResponse(data)
            return render(request,'add_course.html')
    return redirect(reverse('dashboard'))

def add_admin(request):
    if request.user.is_authenticated:
        user = request.user
        pro = profile.objects.filter(user=user).first()
        if int(pro.lev) == 3:
            if request.method =="POST":
                #print(2)
                username = request.POST['username']
                username = username.strip()
                p1 =request.POST['p1']
                p2 = request.POST['p2']
                lev = request.POST['profile']
                regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')  
                #print(username)   
                if  User.objects.filter(username = username):
                    data={
                        'result' : 'error',
                        'message' : 'username taken',
                    }
                    return JsonResponse(data)
                elif ' ' in username:
                    data={
                        'result' : 'error',
                        'message' : 'username cannot contain blank space',
                    } 
                    return JsonResponse(data)                 
                elif p1 != p2:
                    data={
                        'result' :'error',
                        'message' : 'password mismatch',
                    }
                    return JsonResponse(data)
                elif len(p1)<8:
                    data={
                        'result' : 'error',
                        'message' : 'length of password must be 8 character'
                    }
                elif p1.isnumeric():
                    data={
                        'result' :'error',
                        'message' : 'password cannot be entierly numeric',
                    }
                    return JsonResponse(data)
                elif  regex.search(p1) is None: 
                    data={
                        'result':'error',
                        'message': 'Password must contain special character',
                    }
                    return JsonResponse(data)
                else :
                    password = make_password(p1)
                    if is_password_usable(password):
                        r = User(username= username,password = password)
                        r.save()
                        x = profile(user= r,lev = int(lev))
                        x.save()
                        data = {
                            'result' : 'success',
                        }
                        return JsonResponse(data)
            return render(request,'add_admin.html')
    return redirect(reverse('dashboard'))



def log_out(request):
    logout(request)
    return redirect(reverse('getin'))

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect(reverse("getin"))
    user = request.user
    pro = profile.objects.filter(user=user)
    pro = pro.first()
    if int(pro.lev) == 1:
        return render(request,'register_student.html')
    elif int(pro.lev) == 2:
        return render(request,'teacher_dashboard.html')
    elif int(pro.lev) == 3 :
        return render(request,'admin_dashboard.html')
def getin(request):
    if request.method =='POST':
        u = request.POST['uname']
        p = request.POST['password']
        if u is not None and p is not None:
            user = authenticate(request, username=u, password=p)
            pro = profile.objects.filter(user=user)
            if user is not None and pro:
                login(request, user)
                data = {
                    'result' : 'success',
                    'admin' : 'false'
                }
                return JsonResponse(data)
            elif pro :
                message = ""
                if User.objects.filter(username = u):
                    message = "incorrect password"
                else :
                    message = "Username doesn't exist "
                data = {
                    'result' : 'error',
                    'message' : message
                }
                return JsonResponse(data)
            elif user is not None : 
                login(request,user)
                data = {
                    'result' : 'success',
                    'admin' : 'true',
                }
                return JsonResponse(data)
    if request.user.is_authenticated:
        return redirect(reverse("dashboard"))
    return render(request,'home.html')
    