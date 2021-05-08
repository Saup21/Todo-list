from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text=''
        self.fields['password1'].help_text=''
        self.fields['password2'].help_text=''


# class LoginForm(forms.Form):
#     username = forms.CharField(required = True)
#     password = forms.CharField(widget=forms.PasswordInput)
