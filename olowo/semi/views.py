from django.http import HttpResponse, HttpResponseNotFound,\
    response
from django.http import HttpRequest

def index(request):
    a = 1
    if a:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return HttpResponse('<h1>Page was found</h1>') # rendering the template in HttpResponse

def layemo(request):
    r = HttpResponse.content
    return (r)