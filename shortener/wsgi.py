import os
import sys
sys.path.append('/var/www/shortener')
sys.path.append('/var/www/shortener/shortener')
os.environ['DJANGO_SETTINGS_MODULE'] = 'shortener.settings'
os.environ['TZ'] = 'America/Los_Angeles'
from django.core.wsgi import get_wsgi_application
djangoapplication = get_wsgi_application() 
def application(environ, start_response):
    if 'SCRIPT_NAME' in environ:
        del environ['SCRIPT_NAME']
    return djangoapplication(environ, start_response)
