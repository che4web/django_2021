from django.urls import path
from sudentapp.views import index,hello,dish_detail

urlpatterns = [
    path('',hello,name="dish-list"),
    path('<int:pk>/',dish_detail,name="dish-detail"),
]
