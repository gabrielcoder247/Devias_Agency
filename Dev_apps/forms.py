from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30,  required=False, help_text='Optional.')
    username= forms.CharField(max_length=30,required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
  

    class Meta:
        model = User
        fields = ('username', 'name', 'email',
                  'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']  

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['user'] 
        # field = ('title','user',conten)                      
