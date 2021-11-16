from django.contrib import admin
from storageapp.models import Fridge,Item


class ItemInline(admin.TabularInline):
    model = Item

@admin.register(Fridge)
class FridgeAdmin(admin.ModelAdmin):
   inlines = [
       ItemInline
   ]

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
