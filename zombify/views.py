from django.http import HttpResponse

def index(request):
    return HttpResponse("Oh hi, world!")

def result(request):
    return HttpResponse("here's the results page placeholder! PLACEHOLD'd!!!")

def redirect(request, zomburl):
    return HttpResponse("OK so once this works, you'll just get redirected to ZooBorns or whatever destination is linked to zomburl {0}.".format(zomburl))


