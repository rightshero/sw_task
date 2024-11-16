from django.shortcuts import render
from django.http import JsonResponse
from .models import Category
from .utils import get_category_tree
from django.urls import reverse

def category_view(request):
    category_tree = get_category_tree()
    return render(request, 'categories.html', {
        'category_tree': category_tree,
        'create_subcategories_url': reverse('create_subcategories')
    })


def create_subcategories(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        parent_id = request.GET.get('category_id')
        parent = Category.objects.get(id=parent_id)
        
        if not parent.children.exists():
            new_level = parent.level + 1
            prefix = parent.name
            
            subcats = []
            for i in range(1, 3):
                new_cat = Category.objects.create(
                    name=f"SUB {prefix}-{i}",
                    parent=parent,
                    level=new_level
                )
                subcats.append({
                    'id': new_cat.id,
                    'name': new_cat.name,
                    'level': new_level
                })
            return JsonResponse({'subcategories': subcats})
            
    return JsonResponse({'error': 'Invalid request'}, status=400)