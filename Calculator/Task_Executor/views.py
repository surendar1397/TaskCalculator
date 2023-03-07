from django.shortcuts import render , redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home_page(req):
    return render(req,'index.html')

def logins_page(req):
    if req.method == 'GET':
        return render(req,'student_login.html')
    elif req.method == 'POST':
        usr = req.POST.get('name')
        pwd = req.POST.get('pwd')
        passed_user = authenticate(username = usr, password = pwd)
        if passed_user:
            login(req, passed_user)
            passed = req.user.groups.filter(name="Student").exists()
            if passed:
                return render(req,'message.html',{'msg': 'Authentication Passed','href': 'http://127.0.0.1:8000/test', 'caption':'Take test'})
            logout(req)
            return render(req,'message.html',{'msg': 'Authentication Failed(Wrong group)', 'href': 'http://127.0.0.1:8000', 'caption':'Home'})
            
        return render(req,'message.html',{'msg': 'Authentication Failed','href': 'http://127.0.0.1:8000', 'caption':'Home'})


def loginm_page(req):
    if req.method == 'GET':
        return render(req,'master_login.html')
    elif req.method == 'POST':
        usr = req.POST.get('name')
        pwd = req.POST.get('pwd')
        passed_user = authenticate(username = usr, password = pwd)
        if passed_user:
            login(req, passed_user)
            passed = req.user.groups.filter(name="Master").exists()
            print(passed, passed_user, 99999999999)
            if passed:
                return render(req,'message.html',{'msg': 'Authentication Passed','href': 'http://127.0.0.1:8000/addq', 'caption':'Add Question'})
            logout(req)
            return render(req,'message.html',{'msg': 'Authentication Failed(Wrong group)','href': 'http://127.0.0.1:8000', 'caption':'Home'})
            
        return render(req,'message.html',{'msg': 'Authentication Failed', 'href': 'http://127.0.0.1:8000', 'caption':'Home'})

def signups_page(req):
    if req.method == 'GET':
        return render(req,'register.html',{'signup_form': UserCreationForm()})
    elif req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            usr = form.save()
            grp = Group.objects.get(name='Student')
            usr.groups.add(grp)
            return render(req, 'message.html', {'msg': 'User Created', 'href': 'http://127.0.0.1:8000/logins', 'caption':'Student Login'})
        return render(req,'message.html',{'msg' : 'User Creation Failed','href': 'http://127.0.0.1:8000', 'caption':'Home'})
    
def signupm_page(req):
    if req.method == 'GET':
        return render(req,'register.html',{'signup_form': UserCreationForm()})
    elif req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            usr = form.save()
            grp = Group.objects.get(name='Master')
            usr.groups.add(grp)
            return render(req, 'message.html', {'msg': 'User Created', 'href': 'http://127.0.0.1:8000/loginm', 'caption':'Master Login'})
        return render(req,'message.html',{'msg' : 'User Creation Failed','href': 'http://127.0.0.1:8000', 'caption':'Home'})