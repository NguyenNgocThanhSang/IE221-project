from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('manage/', views.manage, name='manage'),
]
