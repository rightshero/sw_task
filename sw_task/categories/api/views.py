from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from sw_task.categories.exceptions import CategoryNotFoundError
from sw_task.categories.services import CategoriesService


CATEGORIES_SERVICE = CategoriesService()

@require_http_methods(['GET'])
def subcategories_api_view(request, category_id):
    try:
        subcategories = CATEGORIES_SERVICE.get_or_create_subcategories(category_id, values=('id', 'name'))
    except CategoryNotFoundError:
        return JsonResponse(status=404, data={'error': 'Category does not exist'})
    return JsonResponse(data=subcategories, safe=False)