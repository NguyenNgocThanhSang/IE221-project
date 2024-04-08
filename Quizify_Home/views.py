from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_login(request):
    return render(request, 'home_login.html')
