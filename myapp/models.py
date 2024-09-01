from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    def create_subcategories(self):
        # Determine the next index for subcategories
        num_existing_subcategories = self.subcategories.count()
        next_index = num_existing_subcategories + 1

        if self.level == 0:
            # For top-level categories
            sub1_name = f"SUB {self.name}{next_index * 2 - 1}"
            sub2_name = f"SUB {self.name}{next_index * 2}"
        else:
        #     # For subcategories
            sub1_name = f"SUB {self.name}-{next_index * 2 - 1}"
            sub2_name = f"SUB {self.name}-{next_index * 2}"

        # Create subcategories
        Category.objects.create(name=sub1_name, parent=self, level=self.level + 1)
        Category.objects.create(name=sub2_name, parent=self, level=self.level + 1)

    def delete_subcategories(self):
        for subcategory in self.subcategories.all():
            subcategory.delete()
