from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from myToDoApp.models import TODO


def signup(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        email = request.POST.get('email')
        password = request.POST.get('pwd')

        User.objects.create_user(username=fnm, email=email, password=password)
        return redirect('/login')
    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        password = request.POST.get('pwd')

        user = authenticate(request, username=fnm, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('/todo')
        else:
            return redirect('/login')

    return render(request, 'login.html')


def todo(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    if request.method == "POST":
        title = request.POST.get('title')
        TODO.objects.create(title=title, user=request.user)
        return redirect('/todo')

    res = TODO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'res': res})
