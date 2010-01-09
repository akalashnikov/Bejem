from django import forms

from bejem.users.models import Member
from bejem.dics.models import City

class LoginForm(forms.Form):
    login = forms.CharField(label='Login')
    password = forms.CharField(widget=forms.PasswordInput)
    rememberMe = forms.BooleanField(label='Remember me', required=False)

class RegistrationForm(forms.Form):
    login = forms.CharField(label='Login')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)
    passwordAgain = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.Form):
    #TODO try build form from users.models.Member
    sex = forms.CharField(max_length=1, widget=forms.Select(choices=Member.SEX_CHOISES), required=False)
    city = forms.ModelChoiceField(City.objects.all(), required=False)



