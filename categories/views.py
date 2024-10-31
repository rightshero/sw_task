from .models import Category
from django.shortcuts import render
from django.http import HttpResponseForbidden, JsonResponse
from django.views.decorators.csrf import csrf_exempt

def category_list(request):
    categories = Category.objects.filter(parent__isnull=True)  # Retrieve only top-level categories
    return render(request, 'rightshero/categories.html', {'categories': categories})


def manage_subcategories(request):
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        parent_category = Category.objects.get(id=parent_id)
        response_data = []

        # Generate specific subcategory names based on parent category
        for i in range(1, 3):  # always two subcategories are created
            subcategory_name = f"SUB {parent_category.name}-{i}"
            subcategory, created = Category.objects.get_or_create(name=subcategory_name, parent=parent_category)
            response_data.append({'id': subcategory.id, 'name': subcategory.name, 'created': created})

        return JsonResponse({'subcategories': response_data})

    elif request.method == 'GET':
        category_id = request.GET.get('category_id')
        subcategories = Category.objects.filter(parent_id=category_id).values('id', 'name')
        return JsonResponse({'subcategories': list(subcategories)})
