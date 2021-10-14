from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,RequestContext
from datetime import datetime as dt
def index(request):
    template = Template("<h1> Hello {{bar}} </h1>")
    context = RequestContext(request)
    context['bar'] = dt.now()
    return HttpResponse(template.render(context))
