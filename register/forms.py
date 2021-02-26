from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
from django.contrib.auth import password_validation



class RegisterForm(UserCreationForm):
    email = forms.EmailField(validators = [validators.validate_email])

    
    class Meta:
        model = User
        fields =["username", "first_name" , "last_name","email", "password", "password1"]
    def adduser (self ,userId):
        self.user = userId
