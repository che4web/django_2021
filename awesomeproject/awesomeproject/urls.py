"""awesomeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from sudentapp.views import index,hello,dish_detail,dish_detail_slug
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index),
    path('dish/',hello,name="dish-list"),
    path('catalog/dish/<int:pk>/',dish_detail,name="dish-detail"),
    re_path('catalog/dish/(?P<slug>[-a-zA-Z0-9_]+)/$',dish_detail_slug,name="dish-detail-slug"),
    path('docs/5.1/layout/containers/',hello),
    path('admin/', admin.site.urls),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
