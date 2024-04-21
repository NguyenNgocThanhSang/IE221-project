from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


class SignUpForm(UserCreationForm):
    '''class tạo form đăng kí tài khoản'''
    email = forms.EmailField(max_length=254, help_text="Required. Inform a valid email address.", required=True)
    role = forms.ChoiceField(choices=[('student', 'Student'), ('teacher', 'Teacher')], required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')
        
    def clean_username(self):
        '''hàm ghi đè username để kiểm tra username đã tồn tại hay chưa'''
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username
    
    def clean_email(self):
        '''hàm ghi đè email để kiểm tra xem email đã tồn tại hay chưa'''
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already taken.")
        return email
    
    def clean_password2(self) -> str:
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("Passwords don't match.")
        return password2
        