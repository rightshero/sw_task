
from django.urls import path
from . import views

urlpatterns = [
    path('', views.top_category_view, name='category_view'),
    path('categories/', views.top_category_view, name='category_list'),  # Root URL directs to /categories
    path('load_subcategories/', views.load_subcategories, name='load_subcategories')
]
