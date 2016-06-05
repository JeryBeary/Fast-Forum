"""
WSGI config for FastForum project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys


root = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, root)


os.environ['DJANGO_SETTINGS_MODULE'] = 'FastForum.settings'


import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
