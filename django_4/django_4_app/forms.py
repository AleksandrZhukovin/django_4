from django import forms
from .models import Project, Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auhth.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'status', 'deadline', 'priority']


# class FilmForm(forms.Form):
#     title = forms.CharField()
#     year = forms.DateField()
#     genre = forms.CharField()
#
#
# class FilmForm1(forms.ModelForm):
#     class Meta:
#         model = Film
#         fields = ['title', 'year', 'genre']
#
#
# class BookForm(forms.Form):
#     title = forms.CharField()
#     year = forms.DateField()
#     author = forms.CharField()
#
#
# class BookForm1(forms.ModelForm):
#     class Meta:
#         model = Film
#         fields = ['title', 'year', 'author']
#         widgets = {'year': forms.DateInput(attrs={'class': 'input1', 'id': 'id1', 'required': False})}
#
#
# class LoginForm(forms.Form):
#     text = forms.CharField(widget=forms.Textarea())
#     password = forms.CharField(widget=forms.PasswordInput())
#     text1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input1', 'id': 'id1', 'required': False}))