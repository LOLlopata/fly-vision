from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from core.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
import os
# views.py


# Create your views here.
def sign_out(request):
    logout(request)
    return redirect('sign_in')

def sign_up(request):
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        if password != repeat_password:
            return render(request, 'core/sign_up.html', {'error': 'неверный логин или пароль'})
    return render(request, 'core/sign_up.html')  

def sign_in(request):
    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if not user is None:
            login(request,user)
            return redirect("")
        else:
            return render(request, 'core/sign_in.html', {"Error":"Подумай как найдешь время на это"})
    return render(request, 'core/sign_in.html') 

@login_required


def profile(request):
    if request.method == 'POST':
        avatar = request.FILES.get('avatar')
        if avatar:

            
            # Сохраняем путь в модели пользователя
            request.user.photo = avatar
            request.user.save()
            
            return redirect('profile')  # Перенаправляем на страницу профиля

    return render(request, 'core/profile.html')

def favorite_movie(request):
    
    return render(request, 'core/favorite_movie.html')