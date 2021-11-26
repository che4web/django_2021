from django.shortcuts import render
from sudentapp.models import Dish
from django.http import HttpResponse,JsonResponse
from django.template import Template,RequestContext
from datetime import datetime as dt
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView
from sudentapp.forms import  DishForm,DishFormModel,DishSearchForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Sum,F

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

def dish_list_json(request):
    queruset = Dish.objects.all()
    form  = DishSearchForm(request.GET)
    if form.is_valid():
        queruset = queruset.filter(name__icontains=form.cleaned_data['name'])
    ret = list(queruset.values('id','name','recipe'))
    return JsonResponse(ret,safe=False)

class DishDetailView(DetailView):
    model = Dish
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        obj = self.get_object()
        ingredients = obj.ingredient_set.all()
        pfc= {
            'protein':0,
            'fat':0,
            'carbohydrate':0,
            'energy':0,
        }
        for i in ingredients:
            pfc['protein']+=i.quantity*float(i.food.protein)
            pfc['fat']+=i.quantity*float(i.food.fat)
            pfc['energy']+=i.quantity*float(i.food.energy)
            pfc['carbohydrate']+=i.quantity*float(i.food.carbohydrate)
        ingredients =ingredients.annotate(
            protein=F('food__protein')*F('quantity'),
            fat=F('food__fat')*F('quantity'),
            carbohydrate=F('food__carbohydrate')*F('quantity'),
            energy=F('food__energy')*F('quantity'),
        )

        pfc_aggr = ingredients.aggregate(
            p=Sum('protein'),
            f=Sum('fat'),
            c=Sum('carbohydrate'),
            e=Sum('energy'),
        )


        context['pfc_aggr']=pfc_aggr
        context['pfc']=pfc
        context['bar']=dt.now
        context['ingredients']=ingredients
        return context

class ProtectListView(LoginRequiredMixin,ListView):
    pass

class DishListView(ProtectListView):
    model = Dish
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['name'] = self.request.GET.get('name')
        return context

    def get_queryset(self):
        queruset = super().get_queryset()
        form  = DishSearchForm(self.request.GET)
        if form.is_valid():
            queruset = queruset.filter(name__icontains=form.cleaned_data['name'])
        return queruset


class DishCreateView(CreateView):
    model = Dish
    fields = "__all__"

class DishUpdateView(UpdateView):
    model = Dish
    fields = "__all__"

class IndexView(TemplateView):
    template_name = "index.html"

