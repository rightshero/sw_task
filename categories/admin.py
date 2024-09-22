from django.contrib import admin

from categories.models import Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    categoryDisplay = ('name', 'parent')


admin.site.register(Category, CategoryAdmin)
