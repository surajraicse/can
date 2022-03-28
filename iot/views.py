
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime

def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
   

def fun(request):
   ml = "<html><body> Life got fucked up.</body></html>"
   return HttpResponse(ml)
