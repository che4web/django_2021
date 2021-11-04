from django.contrib import admin
from sudentapp.models import Dish,Ingredient,Food

# Register your models here.

class IngredientInline(admin.TabularInline):
    model = Ingredient

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
   list_display =['id','name','cooking_time']
   list_filter = ('name', 'cooking_time')
   inlines = [
       IngredientInline
   ]

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass
