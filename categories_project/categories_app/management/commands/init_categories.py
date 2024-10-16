from django.core.management.base import BaseCommand
from categories_app.models import Category


class Command(BaseCommand):
    help = 'Initialize categories with Category A and Category B'

    def handle(self, *args, **kwargs):
        Category.objects.get_or_create(name='Category A')
        Category.objects.get_or_create(name='Category B')
        self.stdout.write(self.style.SUCCESS(
            'Successfully initialized categories'))
