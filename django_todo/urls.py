"""django_todo URL Configuration

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
from django.urls import path
from todo.views import get_todo_list , add_item
#Remeber this .py file is used to do something once our domain URL changes, the URL MUST CHANGE to execute , this is usually done in HTML 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_todo_list, name = "get_todo_list"), # '' means that its basically activated immeditaly as soon as base url is given, so its our home page :)
    path('add/', add_item, name = "add_item")
]
