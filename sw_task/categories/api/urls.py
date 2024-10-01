from django.urls import path
from . import views


urlpatterns = [
    path('categories/<uuid:category_id>/subcategories/', views.subcategories_api_view, name='subcategories-list'),
]