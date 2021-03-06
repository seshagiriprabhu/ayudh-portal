import os
# Local settings for Django projects
# Set all values here before starting the project
# Move this file to the same folder as main settings.py file
# Rename the file as local_settings.py

DEBUG = True
TEMPLATE_DEBUG = DEBUG
PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))

# If running in debug mode, write emails to files.
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = '/tmp'

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Generate a secret key, and don't share it with anybody.
# from django.utils.crypto import get_random_string
# chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
# get_random_string(50, chars)
SECRET_KEY = '00000000000000000000000000000000000000000000000000'

# Password need to changed
#DATABASES = {
#'default': {
#        'ENGINE': 'django.db.backends.ayudh',    # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': 'ayudh',                         # Or path to database file if using sqlite3.
#        'USER': 'ayudhadmin',                    # Not used with sqlite3.
#        'PASSWORD': 'amma123',                   # Not used with sqlite3.
#        'HOST': '',                              # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '',                              # Set to empty string for default. Not used with sqlite3.
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',    # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db/db.db',                         # Or path to database file if using sqlite3.
        'USER': '',                    # Not used with sqlite3.
        'PASSWORD': '',                   # Not used with sqlite3.
        'HOST': '',                              # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                              # Set to empty string for default. Not used with sqlite3.
    }
}
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Kolkata'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_PATH + "/templates",
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
