from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(label='Login')
    password = forms.CharField(widget=forms.PasswordInput)
    rememberMe = forms.BooleanField(label='Remember me', required=False)

class RegistrationForm(forms.Form):
    login = forms.CharField(label='Login')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)
    passwordAgain = forms.CharField(widget=forms.PasswordInput)

