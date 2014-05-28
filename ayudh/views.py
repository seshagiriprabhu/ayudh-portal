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

def logout(request):
    try:
        del request.session['loggedinside']
        del request.session['email']
        request.session.flush()
    except KeyError:
        pass
    return HttpResponseRedirect("/")

def login(request):
    if request.method != "POST":
        return render_to_response('general/login.html',{'page':'login'},RequestContext(request))
    request.session.set_test_cookie()
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
    else:
        return HttpResponse("Please enable cookies and try again")

    input_email = str(request.POST['email'])
    input_pwd = hash_func(str(request.POST['pwd'])).hexdigest()
    login_tuple = Login.objects.all().filter(email=input_email)    
    error_msg = ""
    if login_tuple:
        actual_pwd = str(login_tuple[0].password)
        if input_pwd == actual_pwd:
            request.session['loggedinside'] = True
            request.session['email'] = input_email
            request.session.set_expiry(0)
            #Redirect to home page, but Logged in
            return render_to_response("general/home.html",{},RequestContext(request))
        else:
            error_msg = 'Please enter the right email/password combination'
    else:
        error_msg = 'Please enter the right email/password combination' 
    return render_to_response('general/login.html',{'error_msg': error_msg},context_instance=RequestContext(request))

