from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    path('', views.index, name='index'),  # URL pattern for the index view
    path('', include(router.urls)),  # Include the router URLs
]