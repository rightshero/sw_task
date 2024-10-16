from django.urls import path
from categories_app import views

urlpatterns = [
    path('', views.index, name='index'),
]
