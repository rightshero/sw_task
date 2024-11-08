from django.db import models


class Category(models.Model):
    """
    Represents a category with a name and an optional parent category.

    Attributes:
        name (CharField): The name of the category.
        parent (ForeignKey): A self-referential foreign key to represent the parent category.
                             Null for top-level categories.
    """

    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subcategories",
    )

    def __str__(self) -> str:
        return str(self.name)
