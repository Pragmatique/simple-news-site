from django import forms
from .models import MyUser

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='password')
    class Meta:
        model = MyUser
        fields = ('email', 'password', 'group', 'first_name', 'last_name', 'date_of_birth')
        labels = {
            'email': 'Email',
            'password': 'Password',
            'group': 'Group',
            'first_name': 'First_name',
            'last_name': 'Last_name',
            'date_of_birth': 'Date_of_birth',
        }
        help_texts = {
            'email': 'youremail@domain.com/ required',
            'group': 'required',
        }


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='password')
    class Meta:
        model = MyUser
        fields = ('email', 'password')
        labels = {
            'email': 'Email',
            'password': 'Password',
        }