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
    return render_to_response('registration.html')

def login(request):
    return render_to_response('login.html')

def user_list(request):
    user_list = User.objects.all()
    return render_to_response('users.html', {'user_list': user_list})

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(login__icontains=query) |
            Q(email__icontains=query)
        )
        results = User.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("search.html", {
        "results": results,
        "query": query
    })

