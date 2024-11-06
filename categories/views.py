from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Category

def category_list(request):
    # Load only the two main categories from choices

    categories = Category.objects.filter(name__in=['Category A', 'Category B']) #parent__isnull=True
    return render(request, 'categories/category_list.html', {'categories': categories})

