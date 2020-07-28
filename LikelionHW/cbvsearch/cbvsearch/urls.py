"""cbvsearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
import cbvapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',cbvapp.views.index.as_view(), name = 'index'),
    path('detail/<pk>',cbvapp.views.detail.as_view(), name='detail'),
    path('delete/<pk>',cbvapp.views.delete.as_view(), name = 'delete'),
    path('update/<pk>',cbvapp.views.update.as_view(), name = 'update'),
    path('create',cbvapp.views.create.as_view(), name = 'create'),
]
