from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_page, name='category_page'),
    path('subcategories/<int:category_id>/', views.load_subcategories, name='load_subcategory'),
]