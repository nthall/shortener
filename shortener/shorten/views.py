import random
from datetime import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import Context, loader, RequestContext
from shorten.models import UrlPair

def generate_code():
    pop = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890123456789'
    candidate = ''.join(random.sample(pop, 5))
    return candidate

def check_code(candidate):
    code = candidate
    try: match = UrlPair.objects.get(code__exact=code)
    except (KeyError, UrlPair.DoesNotExist):
        return code
    else: return False

def new_code():
    code = ''
    while not code:
        code = check_code(generate_code())
    return code

#def make_url(request):
#    try:
#        dest_url = request.POST['destination_url']
#    except (KeyError, UrlPair.DoesNotExist):
#        render_to_response('shorten/index.html', {'error_message': "Looks like you didn't enter a valid link. If at first you don't succeed..."}) 
#    else:
#        try:
#            match = UrlPair.objects.get(destination_url__iexact=dest_url)
#        except (KeyError, UrlPair.DoesNotExist):
#            new_url = UrlPair(code=new_code(), destination_url = dest_url, added=datetime.now())
#            new_url.save()
#            result(request, new_url)
#        else:
#            result(request, match, 1)

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def result(request):
    try:
        dest_url = request.POST['destination_url']
    except:
        return render_to_response('index.html', {'error_message': "Looks like you didn't enter a valid link. If at first you don't succeed..."}, context_instance=RequestContext(request)) 
    else:
      #todo: check for empty first, yeesh. and smarter protocol check.
        if dest_url[:7] != 'http://':
            dest_url = 'http://' + dest_url
        try:
            match = UrlPair.objects.get(destination_url__iexact=dest_url)
        except (KeyError, UrlPair.DoesNotExist):
            new_url = UrlPair(code=new_code(), destination_url = dest_url, added=datetime.now())
            new_url.save()
            return render_to_response('result.html', {'url': new_url})
        except:
            raise Http404
        else:
            return render_to_response('result.html', {'url': match, 'alert': "This url has already been shortened! I guess great minds link alike."}) 
    

def send_away(request, code):
    try:
        u = UrlPair.objects.get(code__exact=code)
    except (KeyError, UrlPair.DoesNotExist):
        return render_to_response('index.html', {'error_message': "Oops, that's not a valid shortcode. Maybe you'd like to shorten something else?"}, context_instance=RequestContext(request))
    except:
        raise Http404
    else:
        u.last_accessed = datetime.now()
        try: u.hits = u.hits + 1
        except: u.hits = 1
        u.save()
        return redirect(u.destination_url)

