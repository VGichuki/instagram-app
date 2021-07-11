from django import forms
from django.forms import fields
from .models import Post, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'name', 'caption')

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude =('user', 'followers' ,'following')

# class UserUpdateForm(forms.ModelForm):
#   class Meta:
#     model=User
#     fields=('profile', 'bio')
