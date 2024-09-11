from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full py-3 px-6 rounded-xl',
        'placeholder': 'e.g gideon123'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'w-full py-3 px-6 rounded-xl',
        'placeholder': 'example@gmail.com'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full py-3 px-6 rounded-xl',
        'placeholder': '**********'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full py-3 px-6 rounded-xl',
        'placeholder': '**********'
    }))