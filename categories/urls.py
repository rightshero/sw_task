from django.urls import path
from . import views


urlpatterns = [
    path('', views.category_view, name='category_view'),
    path('create-subcategories/', views.create_subcategories, name='create_subcategories'),
]