from hashlib import sha512 as hash_func

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template
from django.core.context_processors import csrf

from register.models import *

def home(request):
        return render_to_response('general/home.html',{'page':'home'},RequestContext(request))  

def about(request):
    return render_to_response('general/about.html',{'page':'about'},RequestContext(request))
