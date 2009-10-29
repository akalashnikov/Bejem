import datetime

#from django.template.loader import get_template
#from django.template import Context
#from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db.models import Q

from bejem.users.models import User

def index(request):
    current_datetime = datetime.datetime.now()
    #return render_to_response('users.html', locals())
    return render_to_response('index.html', {'current_datetime': current_datetime})

def registration(request):
    q_login = request.GET.get('q_login', '')
    q_email = request.GET.get('q_email', '')
    if q_login and q_email:
        u = User(login=q_login, email=q_email)
        u.save()
    return render_to_response('registration.html', { 'q_login': q_login, 'q_email': q_email })

def login(request):
    query = request.GET.get('q', '')
    result = (len(User.objects.filter(login=query)) != 0)
    return render_to_response('login.html', { 'result': result, 'query': query })

def user_list(request):
    user_list = User.objects.all()
    return render_to_response('users.html', {'user_list': user_list})

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = ( Q(login__icontains=query) | Q(email__icontains=query) )
        results = User.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response('search.html', { 'results': results, 'query': query })

