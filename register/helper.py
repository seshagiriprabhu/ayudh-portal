import os
import urllib
import urllib2
import string

from django.core.mail import send_mail as django_send_mail
from mailer import send_mail as mailer_send_mail

from ayudh.settings import ADMINS_EMAIL

from register.models import *
from register.forms import *

def check_captcha(challenge, response, remote_ip):
    recaptcha_challenge_field = challenge
    recaptcha_response_field = response
    recaptcha_remote_ip = remote_ip
    recaptcha_url = "http://www.google.com/recaptcha/api/verify"
    recaptcha_private_key = "6LdQssASAAAAAMN5M7BgSjQSXnGRwYJKrtATVXXj"
    recaptcha_data = {
                        'privatekey': recaptcha_private_key,
                        'remoteip': recaptcha_remote_ip,
                        'challenge': recaptcha_challenge_field,
                        'response': recaptcha_response_field,
                    }
    recaptcha_encoded_data = urllib.urlencode(recaptcha_data)
    recaptcha_request = urllib2.Request(recaptcha_url, recaptcha_encoded_data)
    recaptcha_response = urllib2.urlopen(recaptcha_request)
    recaptcha_response_data = str(recaptcha_response.readline())
    recaptcha_response_data = recaptcha_response_data.strip()
    #return recaptcha_response_data
    if recaptcha_response_data == 'true':
        return True
    else:
        return False

def notify_new_user(username):
    django_send_mail("New User:" + username,"User registered","Ayudh Notifications",
                                     ADMINS_EMAIL,
                                    fail_silently = False)

def sendmail_after_userreg(email,password):
    email_subject = 'AYUDH \'14 User Registration'
    email_from = 'AYUDH 2014'
    email_message = """
    You have been successfully registered as a USER for AYUDH Amritapuri.
    
    Email   : """ + email + """
    Password: """ + password + """
    
    We look forward to your participation in AYUDH '14. Feel free to ask us any queries
    regarding the same.

    --
    AYUDH Team
    """    

    django_send_mail(email_subject, email_message,email_from,[email], fail_silently=False)
    """
    The code below simply writes the email id to a file.
    This is for ease to add to the google group.
    try:
        file(os.path.join(os.getcwd(), "email_list"), "a").write(email_to + ", ")
    except IOError:
        file(os.path.join(os.getcwd(), "email_list"), "w").write(email_to + ", ")
        """

