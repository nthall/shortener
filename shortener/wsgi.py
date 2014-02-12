import os
import sys
os.system('whoami > /tmp/who.txt')
sys.path.append('/var/www/shortener')
sys.path.append('/var/www/shortener/shortener')
os.environ['DJANGO_SETTINGS_MODULE'] = 'shortener.settings'
os.environ['TZ'] = 'America/Los_Angeles'
import django.core.handlers.wsgi
djangoapplication = django.core.handlers.wsgi.WSGIHandler()
def application(environ, start_response):
    if 'SCRIPT_NAME' in environ:
        del environ['SCRIPT_NAME']
    return djangoapplication(environ, start_response)
