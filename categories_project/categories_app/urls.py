from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns: list[URLPattern] = [
    path('', views.index, name='index'),
    path('category/', views.create_category, name='create_category'),
]
