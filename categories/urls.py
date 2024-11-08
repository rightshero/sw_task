from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('add_subcategory/', views.add_subcategory, name='add_subcategory'),
    path('add_sub_subcategory/', views.add_sub_subcategory, name='add_sub_subcategory'),
]
