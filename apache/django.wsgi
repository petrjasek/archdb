import os
import sys

sys.path.append('/home/petr/dev')
sys.path.append('/home/petr/dev/archdb')

os.environ['DJANGO_SETTINGS_MODULE'] = 'archdb.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
