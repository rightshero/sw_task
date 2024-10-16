from django.shortcuts import render, HttpResponse
from categories_app.models import Category
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    all_categories = Category.objects.filter(parent__isnull=True)
    return render(request, 'index.html', {'categories': all_categories})


@csrf_exempt
@require_http_methods(["POST"])
def create_category(request):
    name = request.POST.get('name')
    parent_id = request.POST.get('parent_id')
    parent = Category.objects.get(id=parent_id)
    all_categories = Category.objects.filter(name=name)
    if parent_id:
        if not all_categories.exists():
            category = Category.objects.create(name=name, parent=parent)
            return JsonResponse({'id': category.id, 'name': category.name})

    category = Category.objects.get(name=name, parent=parent)
    return JsonResponse({'id': category.id, 'name': category.name})
