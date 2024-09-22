from django.http import JsonResponse
from django.shortcuts import render
from categories.models import Category

# Create your views here.


def top_category_view(request):
    categories = Category.objects.filter(parent__isnull=True)
    return render(request, 'categories/category_form.html', {'categories': categories})


def load_subcategories(request):
    if request.method == 'POST':
        parentId = request.POST.get('parentId')
        selectedParent = Category.objects.get(id=parentId)
        # Automatically create unlimited subcategories
        subCategories = Category.objects.filter(parent_id=parentId)
        if not subCategories:
            for i in range(1, 3):
                subCategoryName = f"SUB {selectedParent.name}-{i}" if selectedParent.parent else f"SUB {selectedParent.name}{i}"
                Category.objects.create(name=subCategoryName, parent=selectedParent)
        return JsonResponse(list(subCategories.values('id', 'name')), safe=False)
