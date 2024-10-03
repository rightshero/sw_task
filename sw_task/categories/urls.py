from django.urls import path
from . import views

urlpatterns = [
    path("categories", views.home, name="categories-home"),
]