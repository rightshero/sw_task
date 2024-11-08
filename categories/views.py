from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
def category_list(request):
    # Load only the two main categories from choices
    categories = Category.objects.filter(name__in=['Category A', 'Category B'])  # or 'parent__isnull=True'
    return render(request, 'categories/category_list.html', {'categories': categories})

#level_2

@csrf_protect
def add_subcategory(request):
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')

        try:
            parent_category = Category.objects.get(id=parent_id)
            # Clear existing subcategories
            #parent_category.subcategories.all().delete()
            #generate new subs 
            subcategories = parent_category.add_subcategory()

            if subcategories:
                # Create a response with the new subcategories' names
                subcategory_data = [{'name': subcategory.name} for subcategory in subcategories]
                return JsonResponse({'status': 'success', 'subcategories': subcategory_data})
            else:
                return JsonResponse({'status': 'failed', 'message': 'Subcategories already exist or error occurred.'})
            
        except Category.DoesNotExist:
            return JsonResponse({'status': 'failed', 'message': 'Parent category not found.'})
        
    return JsonResponse({'status': 'failed', 'message': 'Invalid request method.'})

#level_3


@csrf_protect
@require_POST
def add_sub_subcategory(request):
    parent_id = request.POST.get('parent_id')

    if not parent_id or not parent_id.isdigit():
        print("invalid subcategory id")
        return JsonResponse({'error': 'Invalid category ID'}, status=400)

    parent_id = int(parent_id)

    try:
        parent_category = Category.objects.get(id=parent_id)
        # Clear existing sub-subcategories
        parent_category.sub_subcategories.all().delete()

        if parent_category.parent: 
            sub_subcategories = parent_category.add_sub_subcategory()  # Add sub-subcategories

            return JsonResponse({
                'message': 'Sub-subcategories created successfully!',
                'sub_subcategories': [{'id': sub.id, 'name': sub.name} for sub in sub_subcategories]
            })
        
        else:
            return JsonResponse({'error': 'Selected category is not a valid subcategory'}, status=400)
        
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)
