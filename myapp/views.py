from django.shortcuts import render
from django.http import JsonResponse
from .models import Category

def categories_view(request):
    categories = Category.objects.filter(level=0)
    return render(request, 'categories.html', {'categories': categories})

def get_subcategories(request):
    parent_id = request.GET.get('parent_id')
    parent_category = Category.objects.get(id=parent_id)
    
    if parent_category.subcategories.count() == 0:
        parent_category.create_subcategories()
    
    subcategories = parent_category.subcategories.all()
    data = list(subcategories.values('id', 'name'))
    return JsonResponse(data, safe=False)

def remove_subcategories(request):
    parent_id = request.GET.get('parent_id')
    parent_category = Category.objects.get(id=parent_id)
    
    # Delete only sub-subcategories (children) of the given parent_id
    subcategories = parent_category.subcategories.all()
    for subcategory in subcategories:
        subcategory.delete_subcategories()  # This should handle children of subcategory

    subcategories.delete()  # Remove subcategory itself

    return JsonResponse({'status': 'removed'})
