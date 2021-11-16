from django.db import models
from django.contrib.auth.models import User
from sudentapp.models import Food
# Create your models here.


class Fridge(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User,blank=True,null=True,on_delete=models.SET_NULL)

class Item(models.Model):
    fridge = models.ForeignKey(Fridge,on_delete=models.CASCADE,null=True)
    food = models.ForeignKey(Food,on_delete=models.PROTECT,null=True)
    quantity = models.FloatField()
    UNIT_CHOICE = (
        ("KG",'килиграмм'),
        ("G",'грамм'),
        ("U",'штук'),
    )
    unit = models.CharField(max_length=2,choices=UNIT_CHOICE)


