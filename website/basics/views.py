from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def welcome(request):
    return HttpResponse('<h1 style="color:blue;">welcome bruh!</h1>')

def topics(request):
    c=str(datetime.datetime.now())
    return render(request,'topics.html',{'nowVar':c})

def wish(request):
    if 'name' in request.GET:
        name=request.GET['name']
    else:
        name="Xtreme"
    
    return HttpResponse(f'<h1> hi, {name} </h1>')