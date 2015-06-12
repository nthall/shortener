import random
from datetime import datetime
from django.http import Http404
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from shorten.models import UrlPair


def generate_code():
    """
    Generates a candidate shortcode.
    """
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2
    nums = '01234567890123456789' * 2
    pop = letters + nums
    candidate = ''.join(random.sample(pop, 5))
    return candidate


def check_code(candidate):
    """
    Checks whether a candidate code is already in use.
    """
    code = candidate
    try:
        UrlPair.objects.get(code__exact=code)
    except (KeyError, UrlPair.DoesNotExist):
        return code
    else:
        return False


def new_code():
    """
    Gets a valid shortcode (unless all valid codes have been used).
    """
    code = ''
    while not code:
        code = check_code(generate_code())
    return code


def index(request):
    """
    Index.
    """
    return render_to_response('index.html',
                              context_instance=RequestContext(request))


def result(request):
    """
    Handles POST from index page
    """
    if request.POST['destination_url']:
        dest_url = request.POST['destination_url']
        # todo: smarter protocol check.
        if dest_url[:7] != 'http://':
            dest_url = 'http://' + dest_url
        try:
            match = UrlPair.objects.get(destination_url__iexact=dest_url)
        except (KeyError, UrlPair.DoesNotExist):
            new_url = UrlPair(code=new_code(), destination_url=dest_url,
                              added=datetime.now())
            new_url.save()
            return render_to_response('result.html', {'url': new_url})
        except:
            raise Http404
        else:
            data = {'url': match,
                    'alert': ("This url has already been shortened! "
                              "I guess great minds link alike.")}
            return render_to_response('result.html', data)
    else:
        data = {'error_message': ("Looks like you didn't enter a valid link. "
                                  "If at first you don't succeed...")}
        return render_to_response('index.html', data,
                                  context_instance=RequestContext(request))


def send_away(request, code):
    """
    Handles requests for short links
    """
    try:
        url = UrlPair.objects.get(code__exact=code)
    except (KeyError, UrlPair.DoesNotExist):
        data = {'error_message': ("Oops, that's not a valid shortlink. "
                                  "Maybe you'd like to shorten something else?"
                                  )}
        return render_to_response('index.html', data,
                                  context_instance=RequestContext(request))
    except:
        raise Http404
    else:
        url.last_accessed = datetime.now()
        try:
            url.hits = url.hits + 1
        except:
            url.hits = 1
        url.save()
        return redirect(url.destination_url)
