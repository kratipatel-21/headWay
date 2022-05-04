from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from Wayahead.models import *

class SignUp(UserCreationForm):
    password1 = forms.CharField(label = 'Enter Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label = 'Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model=User
        fields=['username', 'first_name','last_name','email']
        labels={'username':'Enter Username', 'first_name':'Enter First Name','last_name':'Enter Last Name','email': 'Enter your E-mail'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
                    'first_name':forms.TextInput(attrs={'class':'form-control'}),
                    'last_name':forms.TextInput(attrs={'class':'form-control'}),
                    'email':forms.EmailInput(attrs={'class':'form-control'})}

class LogIn(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control', 'autofocus':True}))
    password = forms.CharField(label = 'Enter Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
