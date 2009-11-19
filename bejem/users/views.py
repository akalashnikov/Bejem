import datetime

#from django.template.loader import get_template
#from django.template import Context
#from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from bejem.users.models import User
from bejem.users.forms import LoginForm


def index(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))

def registration(request):
    q_login = request.GET.get('q_login', '')
    q_email = request.GET.get('q_email', '')
    if q_login and q_email:
        u = User(login=q_login, email=q_email)
        u.save()
    return render_to_response('registration.html', { 'q_login': q_login, 'q_email': q_email })

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
