from django.db import models

# Create your models here.
class Category(models.Model):
    
    # parent_id = models.CharField(max_length=50,null=True)
    # child_id = models.CharField(max_length=50)

    category_id = models.CharField(max_length=50 )
    category_name = models.CharField(max_length=256)
    parent_id = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        self.category_name