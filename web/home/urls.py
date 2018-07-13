from django.urls import path, include
from . import views 

urlpatterns= [
path(r'', views.index, name= 'index'),
path(r'home/', views.index, name= 'index'),
path(r'contact/', views.contact, name='contact'),
path(r'contact/home/', views.index, name= 'index'),
path(r'work/#/', views.index, name='index'),
path(r'connect/#/', views.index, name='index'),
path(r'work/', views.work, name='work'),
path(r'connect/', views.connect, name='connect'),

]
