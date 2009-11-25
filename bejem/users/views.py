import datetime

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User
from django.contrib.auth import models

from bejem.users.forms import LoginForm
from bejem.users.forms import RegistrationForm

#TODO remove
from bejem.users.models import User

def index(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            passwordAgain = form.cleaned_data['passwordAgain']
            #TODO check unique login and password == passwordAgain
            user = models.User.objects.create_user(username=login, email=email, password=password)
            user.save()
        else:
            return HttpResponseRedirect("/registration")
    else:
        form = RegistrationForm()
    return render_to_response('registration.html', {'form': form})

def login(request):
    #query = request.GET.get('q', '')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            rememberMe = form.cleaned_data['rememberMe']
            if rememberMe:
                request.session.set_expiry(None)
            else:
                request.session.set_expiry(0)
            user = auth.authenticate(username=login, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect("/users/" + login)
            else:
                return HttpResponseRedirect("/registration")
            query = request.POST['username']
    else:
        form = LoginForm()
    #result = (len(User.objects.filter(login=query)) != 0)
    return render_to_response('login.html', {'form': form})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

@login_required
def user_list(request):
    user_list = User.objects.all()
    return render_to_response('users.html', {'user_list': user_list}, context_instance=RequestContext(request))

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = ( Q(login__icontains=query) | Q(email__icontains=query) )
        results = User.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response('search.html', { 'results': results, 'query': query },context_instance=RequestContext(request))
