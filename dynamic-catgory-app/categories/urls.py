from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_view, name='category_view'),
    path('load-subcategories/', views.load_subcategories, name='load_subcategories'),
    path('auto-create-subcategories/', views.auto_create_subcategories, name='auto_create_subcategories'),
]
