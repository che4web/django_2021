from rest_framework import serializers
from sudentapp.models import Dish,Ingredient
class IngredientSerializer(serializers.ModelSerializer):
    food_name = serializers.CharField()
    class Meta:
        model = Ingredient
        fields ="__all__"

class DishSerializer(serializers.ModelSerializer):
    pfc = serializers.DictField()
    #ingredient_set = IngredientSerializer(many=True)
    class Meta:
        model = Dish
        fields ="__all__"
