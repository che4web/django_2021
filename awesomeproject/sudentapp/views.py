from django.shortcuts import render
from sudentapp.models import Dish
from django.http import HttpResponse
from django.template import Template,RequestContext
from datetime import datetime as dt

class myCls:
    name =' для теста'
    def __str__(self):
        return self.name
    def say(self):
        return "hello"

def hello(request):
    dish_list = Dish.objects.all().order_by('-cooking_time')

    return render(request,'foo.html',
                  {'bar':dt.now,
                   'dish_list':dish_list,
                    'hello_from_context':"HELLO",
                   "some_test":" это переменная на питонке"
                   })

def dish_detail(request,pk):
    dish = Dish.objects.get(pk=pk)

    return render(request,'dish_detail.html',
                  {'bar':dt.now,
                   "object":dish
                   })


def dish_detail_slug(request,slug):
    dish = Dish.objects.get(slug=slug)

    return render(request,'dish_detail.html',
                  {'bar':dt.now,
                   "object":dish
                   })




def index(request):
    return render(request,'index.html', {'hello_from_context':"<b>HELLO</b>",
                                         'obj':myCls(),
                                         'some_list':['картошка','лук','Грибы']
                                         })
