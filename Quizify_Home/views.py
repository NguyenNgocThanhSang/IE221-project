from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # hàm redirect chỉ nhận url pattern
            return redirect('home')  # Chuyển hướng đến trang chính sau khi đăng nhập thành công
        else:
            return render(request, 'signin.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'signin.html')

def signout(request):
    logout(request)
    return redirect('signin.html')

def home(request):
    return render(request, 'home.html')