from django.shortcuts import render
from sudentapp.models import Dish
from django.http import HttpResponse
from django.template import Template,RequestContext
from datetime import datetime as dt
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView

def index(request):
    return render(request,'index.html',{})

def create_view(request):
    if request.method == 'GET':
        return render(request,'sudentapp/dish_form.html',{})
    elif request.method == 'POST':
        context={}
        name = request.POST['name']
        recipe= request.POST['recipe']
        cooking_time = request.POST['cooking_time']
        typ = request.POST['typ']
        if Dish.objects.filter(name=name).exists():
            context['error'] = "Такое блюдо уж есть"
            context['name'] = name
            context['recipe'] = recipe
            context['cooking_time'] = cooking_time
        else:
            dish = Dish(
                name=name,
                recipe=recipe,
                cooking_time=cooking_time,
                typ=typ
            )
            dish.save()
            context['dish'] =dish
        return render(request,'sudentapp/dish_form.html',context)

class DishDetailView(DetailView):
    model = Dish
    def get_context_date(self,*args,**kwargs):
        context = super().get_CreateViewcontext_date(*args,**kwargs)
        context['bar']=dt.now
        return context

class DishListView(ListView):
    model = Dish

class DishCreateView(CreateView):
    model = Dish
    fields = "__all__"

class IndexView(TemplateView):
    template_name = "index.html"

