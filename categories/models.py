from django.db import models

class Category(models.Model):
    CATEGORY_CHOICES = (
        ('Category A', 'Category A'),
        ('Category B', 'Category B'),
    )
    
    name = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.name

    def get_subcategories(self):
        """Fetch direct subcategories of the current category."""
        return self.subcategories.all()

    def get_descendants(self):
        """Recursively get all subcategories (descendants) of the current category."""
        descendants = []
        def get_recursive_descendants(category):
            subcategories = category.get_subcategories()
            for subcategory in subcategories:
                descendants.append(subcategory)
                get_recursive_descendants(subcategory)
        get_recursive_descendants(self)
        return descendants
