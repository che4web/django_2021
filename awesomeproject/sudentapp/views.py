from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,RequestContext
from datetime import datetime as dt

def index(request):
    return render(request,'foo.html',{'bar':dt.now})
