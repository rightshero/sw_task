from django.http import JsonResponse
from django.shortcuts import render
from .models import Category

def category_page(request):
    # Load only top-level categories (parent is null)
    categories = Category.objects.filter(parent__isnull=True)
    return render(request, 'categories/category_page.html', {'categories': categories})

def load_subcategories(request):
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        parent_category = Category.objects.get(id=parent_id)
        
        # Check if subcategories exist for this category
        subcategories = Category.objects.filter(parent_id=parent_id)

        # If no subcategories exist, automatically create two subcategories
        if not subcategories.exists():
            Category.objects.create(name=f"SUB Category {parent_category.name}1", parent=parent_category)
            Category.objects.create(name=f"SUB Category {parent_category.name}2", parent=parent_category)
            # Reload subcategories after creation
            subcategories = Category.objects.filter(parent_id=parent_id)

        return JsonResponse(list(subcategories.values('id', 'name')), safe=False)
    return JsonResponse({'error': 'Invalid request'}, status=400)
