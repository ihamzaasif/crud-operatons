"""product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from product import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ProductView.as_view()),
    path('<int:pk>',views.Product_manage.as_view()),
    path('<str:pk>', views.Product_manage.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)













# from django.contrib import admin
# from django.urls import path
# from .import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.show_product, name="product"),
#     path('post/',views.post, name="add_product"),
#     path('get/<int:id>/', views.get, name="get_product"),
#     path('put/<int:id>/', views.put, name="update_product"),
#     path('delete/<int:id>/', views.delete, name="delete"),

