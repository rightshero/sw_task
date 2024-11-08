from django.contrib import admin
from . import models

@admin.register(models.Category)
class ProductAdmin(admin.ModelAdmin):
    pass