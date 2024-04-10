from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('Quizify_Home/', views.home, name='home'),
]
