from .models import Category

def get_category_tree(category=None):
    """Recursively build category tree"""
    if category is None:
        categories = Category.objects.filter(parent=None)
    else:
        categories = Category.objects.filter(parent=category)
    
    result = []
    for cat in categories:
        children = get_category_tree(cat)
        result.append({
            'id': cat.id,
            'name': cat.name,
            'level': cat.level,
            'children': children
        })
    return result