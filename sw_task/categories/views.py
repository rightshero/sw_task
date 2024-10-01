from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .services import CategoriesService

CATEGORIES_SERVICE = CategoriesService()

@csrf_exempt
def home(request):
    categories = CATEGORIES_SERVICE.get_categories()
    return render(request, "categories/categories.html", {"categories": categories})
