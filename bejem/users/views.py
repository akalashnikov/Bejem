import datetime

#from django.template.loader import get_template
#from django.template import Context
#from django.http import HttpResponse
from django.shortcuts import render_to_response

from bejem.users.models import User

def index(request):
    current_datetime = datetime.datetime.now()
    return render_to_response('users.html', {'current_datetime': current_datetime})
    #return render_to_response('users.html', locals())
