from django.db import models

class Category(models.Model):
    CATEGORY_CHOICES = (
        ('Category A', 'Category A'),
        ('Category B', 'Category B'),
    )

    name = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')

    class Meta:
        verbose_name_plural = "categories"
        ordering = ['name']

    def __str__(self):
        return self.name

    # Method to generate and add exactly two subcategories at the same time
    def add_subcategory(self):
        #delete existing subcategories (children)
        self.children.all().delete()
        # Check if there are no subcategories already
        siblings_count = self.parent.children.count() if self.parent else 0
        subcategories = []  # Initialize an empty list for subcategories
        if siblings_count == 0:  # Only create subcategories if none exist
            # Create both subcategories together
            subcategory_1 = Category.objects.create(name=f"SUB {self.name}1", parent=self)
            subcategory_2 = Category.objects.create(name=f"SUB {self.name}2", parent=self)
            subcategories.extend([subcategory_1, subcategory_2])  # Add both subcategories to the list
        # Return the list of subcategories created
        return subcategories if subcategories else None

    # New method to generate sub-subcategories (subcategories of subcategories)
    def add_sub_subcategory(self):
        #delete existing sub-subcategories of each child (subcategory)
        for subcategory in self.children.all():
            subcategory.children.all().delete()
        # Check if there are subcategories to work with
        if not self.children.exists():
            return None  # No subcategories to generate sub-subcategories from

        sub_subcategories = []  # Initialize an empty list for sub-subcategories
        
        # Iterate over each subcategory and create two sub-subcategories
        for subcategory in self.children.all():
            sub_subcategory_1 = Category.objects.create(name=f"SUB SUB {subcategory.name}-1", parent=subcategory)
            sub_subcategory_2 = Category.objects.create(name=f"SUB SUB {subcategory.name}-2", parent=subcategory)
            sub_subcategories.extend([sub_subcategory_1, sub_subcategory_2])  # Add both sub-subcategories

        # Return list of created sub-subcategories
        return sub_subcategories if sub_subcategories else None

    # Static method to get the main categories (Category A and B)
    @classmethod
    def get_main_categories(cls):
        return cls.objects.filter(parent__isnull=True)
