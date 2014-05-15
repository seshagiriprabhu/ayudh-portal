import os
import sys
sys.path.append('/usr/local/django')
sys.path.append('/var/www')
sys.path.append('/var/www/ayudh')
sys.path.append('/var/www/ayudh/media')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ayudh.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

path = '/var/www/ayudh'
if path not in sys.path:
    sys.path.append(path)
