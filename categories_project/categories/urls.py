from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_page, name='category_page'),
    path('load-subcategories/', views.load_subcategories, name='load_subcategories'),
]
