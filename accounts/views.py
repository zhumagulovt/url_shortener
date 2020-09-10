from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


def registration(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():

                    return render(request, 'accounts/registration.html',
                                {'error': 'Имя пользователя занято'})
        
        if User.objects.filter(email=email).exists():

                    return render(request, 'accounts/registration.html',
                                {'error': 'Электронная почта уже используется'})

        user = User.objects.create_user(username, email, password)
        login(request, user)
        return redirect("/")

    else:

        return render(request, "accounts/registration.html")

def loginView(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
        
        if user is not None:
            login(request, user)
            try:
                return redirect(request.GET['next'])
            except:
                pass
        else:
            return render(request, "accounts/login.html", 
            {'error': 'Неправильное имя пользователя или пароль'})
        return redirect("/")

    else:

        return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect('/')
