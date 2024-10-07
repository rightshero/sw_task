from django.urls import path
from assessment_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_child/', views.get_child, name='get_child'),
    path('get_all_children/', views.get_all_children, name='get_all_children'),
]