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
from django.urls import path,re_path,include
from sudentapp.views import IndexView
from django.conf import settings
from django.conf.urls.static import static

from  django.contrib.auth.views import LoginView
from rest_framework.routers import DefaultRouter
from sudentapp.views import DishViewSet,IngredientViewSet

router = DefaultRouter()
router.register(r'dish', DishViewSet)
router.register(r'ingredient',IngredientViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('',IndexView.as_view()),
    path('accounts/login/',LoginView.as_view(template_name="login.html"),name="login"),
    path('dish/',include("sudentapp.urls")),
    path('admin/', admin.site.urls),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
