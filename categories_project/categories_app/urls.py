from django.urls import path
from django.urls.resolvers import URLPattern
from categories_app import views

urlpatterns: list[URLPattern] = [
    path('', views.index, name='index'),
    path('category/', views.create_category, name='create_category'),
]
