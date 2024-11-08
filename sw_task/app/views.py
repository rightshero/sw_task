from django.shortcuts import render
from django.http import JsonResponse
from .models import Category

def index(request):
    """
    Renders the main page with the top-level categories (Category A, Category B, etc.).
    """
    categories = Category.objects.filter(parent=None)  # Fetch top-level categories
    return render(request, 'category_page.html', {'categories': categories})


def load_subcategories(request):
    """
    AJAX view to load subcategories based on selected category.
    """
    parent_id = request.GET.get('parent_id')
    subcategories = Category.objects.filter(parent_id=parent_id)  # Fetch subcategories

    # Prepare data in JSON format
    data = {
        'subcategories': [
            {'id': subcategory.id, 'name': subcategory.name} for subcategory in subcategories
        ]
    }
    return JsonResponse(data)
