from django.core.management.base import BaseCommand
from sw_task.categories.services import CategoriesService


CATEGORY_SERVICE = CategoriesService()

class Command(BaseCommand):
    help = 'Create categories'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, nargs='?', help='Number of categories to create')
    
    def handle(self, *args, **kwargs):
        count = kwargs.get('--count')
        if not count:
            count = 0
        data = [
            {"name": f"Category {i}"}
            for i in range(1, count + 1)
        ]
        created_categories = CATEGORY_SERVICE.create_categories(data)
        self.stdout.write(self.style.SUCCESS(f"Created {len(created_categories)} categories"))
        for category in created_categories:
            self.stdout.write(self.style.SUCCESS(f"Category: {category.name}"))
