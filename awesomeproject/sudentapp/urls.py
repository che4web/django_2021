from django.urls import path
from sudentapp.views import( DishListView,
                            DishDetailView,
                            DishCreateView,
                            create_view,
                            DishUpdateView,
                            dish_list_json,
                            food_list_json,
                            like
                            )

urlpatterns = [
    path('',DishListView.as_view(),name="dish-list0"),
    path('like/',like,name="dish-like"),
    path('json/',dish_list_json,name="dish-list-json"),
    path('food/json/',food_list_json,name="food-list-json"),
    #path('create',DishCreateView.as_view(),name="dish-create"),
    path('create',create_view,name="dish-create0"),
    path('<int:pk>/class',DishDetailView.as_view(),name="dish-detail0"),
    path('<int:pk>/update',DishUpdateView.as_view(),name="dish-update0"),
]
