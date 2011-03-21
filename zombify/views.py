from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, loader, RequestContext
from zombify.models import Zomburl

def index(request):
    return render_to_response('zombify/index.html')

def result(request, zomblink):
# still building this... but at least now it theoretically checks for the csrf_token.
# still need to build the view also.
#    z = get_object_or_404(Zomburl, zomblink = zomblink)
#    return render_to_response('zombify/result.html', {'result': z}, context_instance=RequestContext(request))    
    return HttpResponse("here's the results page placeholder! PLACEHOLD'd!!!")

def redirect(request, zomblink):
    z = get_object_or_404(Zomburl, zomblink = zomblink)
    return HttpResponse("OK so once this works, you'll just get redirected:<br><br> {0}.".format(z))


