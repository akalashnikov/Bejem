from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(label='Login')
    password = forms.CharField(widget=forms.PasswordInput)
    rememberME = forms.BooleanField(label='Remember me', required=False)

