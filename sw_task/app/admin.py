from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')   
    list_filter = ('parent',)                         
    ordering = ('parent', 'name')                     

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('parent')            

admin.site.register(Category, CategoryAdmin)
