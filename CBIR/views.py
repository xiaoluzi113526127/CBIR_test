import datetime

from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.
def sayHello(request):
    s = 'Hello World!'
    current_time = datetime.datetime.now()
    html = '<html><head></head><body><h1> %s </h1><p> %s </p></body></html>' % (s, current_time)
    return HttpResponse(html)
def showInformation(request):
     list = [{id: 1, 'name': 'Jack'}, {id: 2, 'name': 'Rose'}]
     return render_to_response('information.html',{'students': list})