from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children', on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
