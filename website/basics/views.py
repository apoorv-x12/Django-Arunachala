from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome(request):
    return HttpResponse('<h1 style="color:blue;">welcome bruh!</h1>')
