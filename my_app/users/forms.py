from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label = "Password",
        widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
            }),
    )

    password2 = forms.CharField(
        label = "Repeat password",
        widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Repeat password'
            }),
    )
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                }),
        }

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
        }),
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }),
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
        }),
    )
