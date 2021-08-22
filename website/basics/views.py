from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def welcome(request):
    return HttpResponse('<h1 style="color:blue;">welcome bruh!</h1>')

def topics(request):
    c=str(datetime.datetime.now())
    return render(request,'topics.html',{'nowVar':c})