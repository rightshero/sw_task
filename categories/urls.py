from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    #path('load-subcategories/<int:category_id>/', views.load_subcategories, name='load_subcategories'),
]
