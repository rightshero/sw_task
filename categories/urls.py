from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.category_view, name='category_view'),
    path('create-subcategories/', views.create_subcategories, name='create_subcategories'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)