from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  # Default form for user creation
from apps.userprofile.models import Profile


class SignUpform(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text='Please enter First name')
    last_name = forms.CharField(max_length=30, help_text='Please enter last name')
    email = forms.EmailField(max_length=300, help_text='Please enter valid email address')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'phone_number', 'birth_date', 'profile_image']
