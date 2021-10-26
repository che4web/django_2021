from django.contrib import admin
from sudentapp.models import Dish,Food

# Register your models here.

class FoodInline(admin.TabularInline):
    model = Food

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
   list_display =['id','name','cooking_time']
   list_filter = ('name', 'cooking_time')
   inlines = [
        FoodInline
   ]

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass
