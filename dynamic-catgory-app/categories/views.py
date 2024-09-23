from django.shortcuts import render
from .models import Category

def category_view(request):
    categories = Category.objects.filter(parent__isnull=True)
    return render(request, 'categories/category_page.html', {'categories': categories})
