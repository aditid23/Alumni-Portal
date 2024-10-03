from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'location', 'date_of_birth']

class CreateUserForm(UserCreationForm):
 class Meta:
    model=User
    fields=["username","email","password1","password2"]

class UserPasswordChangeForm(PasswordChangeForm):
    # Add any customizations here
    pass