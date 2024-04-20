from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text="Required. Inform a valid email address.", required=False)
    role = forms.ChoiceField(choices=[('student', 'Student'), ('teacher', 'Teacher')], required=False)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username
    
    def clean_email(self):
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
    
    def save(self, commit: bool = True) -> Any:
        '''ghi đè hàm save để tạo mật khẩu đơn giản'''
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.role = self.cleaned_data.get('role')
        if commit:
            user.save()
        return user
    
        