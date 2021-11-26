from django.urls import path
from sudentapp.views import( DishListView,
                            DishDetailView,
                            DishCreateView,
                            create_view,
                            DishUpdateView,
                            dish_list_json
                            )

urlpatterns = [
    path('',DishListView.as_view(),name="dish-list"),
    path('json/',dish_list_json,name="dish-list"),
    #path('create',DishCreateView.as_view(),name="dish-create"),
    path('create',create_view,name="dish-create"),
    path('<int:pk>/class',DishDetailView.as_view(),name="dish-detail"),
    path('<int:pk>/update',DishUpdateView.as_view(),name="dish-update"),
]
