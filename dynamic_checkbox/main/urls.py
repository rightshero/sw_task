from django.urls import path

from . import views

urlpatterns=[
    # path("", views.index, name="index"),
    path("", views.home, name="home"),
    path('update_checkbox/', views.update_checkbox, name='update_checkbox'),  # For AJAX
    path('clear_checkboxes/', views.clear_checkboxes, name='clear_checkboxes'), # For AJAX-> used when page is refreshed

]