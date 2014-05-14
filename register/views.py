from hashlib import sha512 as hash_func

from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template
from django.core.context_processors import csrf
from django.views.csrf import csrf_failure
from django.utils import simplejson

from register.models import User
from register.forms import *
from register.helper import *
from register.lists import LIST_OF_STATES as statelist
from django.http import Http404
import datetime


def error_key(request):
    return render_to_response('keyerror.html',{'reason':'bloob'},RequestContext(request))
    
def csrf_failure(request, reason=""):
    return render_to_response('keyerror.html',{'reason':reason}, RequestContext(request))

def logged_in(request):
    try:
        if request.session['loggedinside']:
            return True
        else:
            return False
    except KeyError:
        return False
    
def viewtemplate(request):
    return render_to_response('general/index.html',RequestContext(request))

def register(request):
    return render_to_response('register/register.html',RequestContext(request))
#    return render_to_response('register/registerclosed.html',RequestContext(request))

def registeruser(request):
    try:
        if logged_in(request):
            raise Http404() 
        context_instance=RequestContext(request)
        if request.method == 'POST':
            user_form = UserForm(request.POST)
            recaptcha_challenge_field = request.POST['recaptcha_challenge_field']
            recaptcha_response_field = request.POST['recaptcha_response_field']
            recaptcha_remote_ip = ""
            captcha_is_correct = check_captcha(recaptcha_challenge_field, 
                                                recaptcha_response_field,
                                                recaptcha_remote_ip)
            user_is_valid = user_form.is_valid()
        
            if user_is_valid and captcha_is_correct:
                cleaned_user_data = user_form.cleaned_data
                cleaned_username = cleaned_user_data['name']
                cleaned_email = cleaned_user_data['email']
                user_form.save()
            
                sendmail_after_userreg(cleaned_username, cleaned_username, cleaned_email)
                notify_new_user(cleaned_username)
                return HttpResponseRedirect('/register/user/success/')

            else:
                captcha = 'true'
                if not captcha_is_correct and user_is_valid:
                    captcha = 'false'
                return render_to_response('register/registeruser.html',
                                            {'user_form':user_form,
                                            'page':'register',
                                            'captcha':captcha},
                                        RequestContext(request))
    
        return render_to_response('register/registeruser.html', 
                                                    {'user_form' : UserForm(),
                                                        'page':'register'},
                                                        RequestContext(request))
    except KeyError:
        return error_key(request)

def userregistrationsuccess(request):
        #Prevent CSRF Attacks
        return render_to_response('register/successful.html',{},RequestContext(request))

def visualreg(request):
    users = User.objects.all()
    user_list = {}

    for (counter, item) in enumerate(users):
        user_list[counter+1] = [item.name, item.department, item.position, item.contact_no, item.email]

    return render_to_response('register/userregvisual.html',{'user_list':user_list},RequestContext(request))
