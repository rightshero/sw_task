def create_initial_categories():
    from .models import Category

    # Check if categories already exist
    if not Category.objects.filter(name='Category A').exists():
        Category.objects.create(name='Category A')

    if not Category.objects.filter(name='Category B').exists():
        Category.objects.create(name='Category B')