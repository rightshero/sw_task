from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """
    MPTTModel is a Django model used for efficient storage and retrieval
    of hierarchical data, like categories and their subcategories.
    It optimizes queries and operations on deep or complex trees
    by using a Modified Preorder Tree Traversal algorithm,
    making it ideal for applications with extensive nested structures.
    """

    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
