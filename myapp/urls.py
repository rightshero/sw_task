from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories_view, name='categories_view'),
    path('get_subcategories/', views.get_subcategories, name='get_subcategories'),
    path('remove_subcategories/', views.remove_subcategories, name='remove_subcategories'),
]
