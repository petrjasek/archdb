import os
import sys

sys.path.append('/var/www/')
sys.path.append('/var/www/archdb')

os.environ['DJANGO_SETTINGS_MODULE'] = 'archdb.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
