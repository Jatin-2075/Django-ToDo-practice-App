from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from myToDoApp import models
from myToDoApp.models import TODO

def signup(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        email = request.POST.get('email')
        password = request.POST.get('pwd')
        print(fnm, email, password)
        my_user=User.objects.create_user(fnm,email,password)
        my_user.save()
        return redirect('/login')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        password = request.POST.get('pwd')
        print(fnm, password)
        user = authentication(request, username = fnm, password = password)
        if user is not None :
            login (request, user)
            return redirect('/todo')
        else : 
            return redirect('/login')
    return render(request, 'login.html')

def todo(request):
    if request.method == "POST":
        title = request.POST.get('title')
        print(title)
        obj = models.TODO(title=title, user=request.user)
        obj.save()
        res = models.TODO.objects.filter(user=request.user).order_by('-date')
        return redirect('/todo', {'res' : res })
    res = models.TODO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'res':res})

def edit_todo(request):
    pass