from django.db import models
from django.urls import reverse
from easy_thumbnails.fields import ThumbnailerImageField

# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название блюда",unique=True)
    slug = models.CharField(max_length=255,verbose_name="slug",blank=True)
    recipe = models.TextField(verbose_name="Рецепт")
    cooking_time = models.IntegerField()
    TYP_CHOICES =(
        ("S",'Суп'),
        ("G",'Гарнир'),
    )
    typ = models.CharField(max_length=2,choices=TYP_CHOICES)
    photo  = ThumbnailerImageField(blank=True,null=True)

    def some_f(self):
        return "hello "+self.name
    def __str__(self):
        return self.name
    def get_photo_url(self):
        return self.photo['big'].url if self.photo else ''

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
        ordering = ['-name','cooking_time']
        permissions = [
            ("my_permission","Это мое особое разрешение"),
        ]

    def get_absolute_url(self):
        return reverse('dish-detail',kwargs={'pk':self.pk})
        #return reverse('dish-detail',kwargs={'pk':self.id})

    def save(self,*args,**kwargs):
        print("hello")
        ret = super().save(*args,**kwargs)
        print("afret real save")
        return ret


class Food(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название продукта")
    protein = models.FloatField(default=0,verbose_name="Протеинов на 100г")
    fat = models.FloatField(default=0,verbose_name="Жиров на 100г")
    carbohydrate = models.FloatField(default=0,verbose_name="Жиров на 100г")
    energy  =  models.FloatField(default=0,verbose_name="ккал на 100г")
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    dish = models.ForeignKey(Dish,on_delete=models.CASCADE,null=True)
    food = models.ForeignKey(Food,on_delete=models.PROTECT,null=True)
    quantity = models.FloatField()
    UNIT_CHOICE = (
        ("KG",'килиграмм'),
        ("G",'грамм'),
        ("U",'штук'),
    )
    unit = models.CharField(max_length=2,choices=UNIT_CHOICE)

from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases_global

saved_file.connect(generate_aliases_global)
