from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader

def index(request):
    return render_to_response('zombify/index.html')

def result(request):
    return HttpResponse("here's the results page placeholder! PLACEHOLD'd!!!")

def redirect(request, zomburl):
    return HttpResponse("OK so once this works, you'll just get redirected to ZooBorns or whatever destination is linked to zomburl {0}.".format(zomburl))


