from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Category

def category_view(request):
    categories = Category.objects.filter(parent__isnull=True)
    return render(request, 'categories/Category_page.html', {'categories': categories})


def load_subcategories(request):
    parent_id = request.GET.get('parent_id')
    subcategories = Category.objects.filter(parent_id=parent_id)
    data = []
    for subcategory in subcategories:
        data.append({
            'id': subcategory.id,
            'name': subcategory.name,
            'has_children': subcategory.children.exists()
        })
    return JsonResponse(data, safe=False)

@csrf_exempt
def auto_create_subcategories(request):

    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        parent_category = Category.objects.get(id=parent_id)
        num_subcategories = 2  
        new_subcategories = []
        for i in range(1, num_subcategories + 1):
            new_name = generate_subcategory_name(parent_category, i)
            new_subcategory = Category.objects.create(name=new_name, parent=parent_category)
            new_subcategories.append({
                'id': new_subcategory.id,
                'name': new_subcategory.name
            })
        return JsonResponse(new_subcategories, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)

def generate_subcategory_name(parent_category, index):
    new_name = f"{parent_category.name} > Sub {index}"
    return new_name