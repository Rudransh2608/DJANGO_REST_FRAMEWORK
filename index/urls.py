from django.contrib import admin
from django.urls import path, include 

from . import views
from .views import *

urlpatterns = [
     path('', StudentAPI.as_view()),
     path('REQUESTTOKEN/', tokenAU.as_view()),
     path('n/', views.index_new),
]



