from django.urls import path, include
from . import views 

urlpatterns= [
path(r'about/', views.about, name= 'about')]