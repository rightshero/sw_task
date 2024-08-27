from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Category
from drf_spectacular.utils import extend_schema


class IndexView(View):
    """
    This view fetches all categories from the database and renders them
    """

    @extend_schema(
        summary="Fetch all categories",
        description="Retrieve all root categories without any parent.",
        responses={200: "HTML content rendering the categories"}
    )
    def get(self, request, *args, **kwargs):
        categories = Category.objects.filter(parent=None)
        context = {'categories': categories}
        return render(request, 'categories/index.html', context)


@method_decorator(csrf_exempt, name='dispatch')
class CreateCategoryView(View):
    """
    This view creates a new category and returns its ID and name
    """

    @extend_schema(
        summary="Create a new category",
        description="Create a new category under a specified parent or as a root category.",
        request={"name": "string", "parent_id": "integer"},
        responses={200: "Category ID and Name"}
    )
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        parent_id = request.POST.get('parent_id')

        if not name:
            return JsonResponse({'success': False, 'error': 'Name is required.'})

        parent = None
        if parent_id:
            try:
                parent = Category.objects.get(id=parent_id)
            except Category.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Parent category not found.'})

        category = Category.objects.filter(name=name, parent=parent).first()

        if category:
            return JsonResponse({'success': True, 'category': {'id': category.id, 'name': category.name}})
        else:
            category = Category.objects.create(name=name, parent=parent)
            return JsonResponse({'success': True, 'category': {'id': category.id, 'name': category.name}})


@method_decorator(csrf_exempt, name='dispatch')
class CreateSubCategoryView(View):
    """
    This view creates two subcategories for a given parent category
    """

    @extend_schema(
        summary="Create subcategories",
        description="Create two subcategories under a specified parent category.",
        request={"parent_id": "integer"},
        responses={200: "List of subcategories"}
    )
    def post(self, request, *args, **kwargs):
        parent_id = request.POST.get('parent_id')
        try:
            parent = Category.objects.get(id=parent_id)
            subcategories = parent.get_children()

            if subcategories.exists():
                subcategories_list = [{'id': subcat.id, 'name': subcat.name} for subcat in subcategories]
                return JsonResponse({'success': True, 'subcategories': subcategories_list})
            else:
                subcat1 = Category.objects.create(name=f"SUB {parent.name}1", parent=parent)
                subcat2 = Category.objects.create(name=f"SUB {parent.name}2", parent=parent)
                subcategories_list = [
                    {'id': subcat1.id, 'name': subcat1.name},
                    {'id': subcat2.id, 'name': subcat2.name}
                ]
                return JsonResponse({'success': True, 'subcategories': subcategories_list})
        except Category.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Parent category not found.'})


@method_decorator(csrf_exempt, name='dispatch')
class RemoveSubCategoryView(View):
    """
    This view removes all subcategories from a given parent category
    """

    @extend_schema(
        summary="Remove subcategories",
        description="Remove all subcategories under a specified parent category.",
        request={"parent_id": "integer"},
        responses={200: "Success status"}
    )
    def post(self, request, *args, **kwargs):
        parent_id = request.POST.get('parent_id')
        try:
            parent = Category.objects.get(id=parent_id)
            subcategories = parent.get_children()
            subcategories.delete()  # Delete subcategories from the database
            return JsonResponse({'success': True})
        except Category.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Parent category not found.'})
