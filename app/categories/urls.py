from django.urls import path
from .views import IndexView, CreateCategoryView, CreateSubCategoryView, RemoveSubCategoryView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create_category/', CreateCategoryView.as_view(), name='create_category'),
    path('create_subcategory/', CreateSubCategoryView.as_view(), name='create_subcategory'),
    path('remove_subcategory/', RemoveSubCategoryView.as_view(), name='remove_subcategory'),
]
