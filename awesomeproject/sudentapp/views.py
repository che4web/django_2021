from django.shortcuts import render
from sudentapp.models import Dish
from django.http import HttpResponse
from django.template import Template,RequestContext
from datetime import datetime as dt
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView
from sudentapp.forms import  DishForm,DishFormModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request,'index.html',{})

@login_required
def create_view(request):
    if request.method == 'GET':
        form = DishFormModel()
        return render(request,'sudentapp/dish_form.html',{'form':form})
    elif request.method == 'POST':
        context={}
        form = DishFormModel(request.POST)
        context['form'] =form
        if form.is_valid():
            dish = form.save()
            context['dish'] =dish
        else:
            pass
        return render(request,'sudentapp/dish_form.html',context)


class DishDetailView(DetailView):
    model = Dish
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['bar']=dt.now
        return context

class ProtectListView(LoginRequiredMixin,ListView):
    pass

class DishListView(ProtectListView):
    model = Dish

class DishCreateView(CreateView):
    model = Dish
    fields = "__all__"

class DishUpdateView(UpdateView):
    model = Dish
    fields = "__all__"

class IndexView(TemplateView):
    template_name = "index.html"

