from django.db import models

# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название блюда")
    recipe = models.TextField(verbose_name="Рецепт")
    cooking_time = models.IntegerField()

    def some_f(self):
        return "hello "+self.name
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"

class Food(models.Model):
    dish = models.ForeignKey(Dish,on_delete=models.CASCADE)
    name = models.CharField(max_length=255,verbose_name="Название продукта")
    quantity = models.FloatField(verbose_name=" колличество ")

