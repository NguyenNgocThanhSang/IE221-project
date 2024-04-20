from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib.auth.models import Group

# Create your views here.

def signin(request):
    '''view đăng nhập trang web'''
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
    
def signup(request):
    '''view đăng ký tài khoản'''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')
            group = Group.objects.get(name=role)
            group.user_set.add(user)
            return redirect('signin')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('signin.html')

def home(request):
    return render(request, 'home.html')


