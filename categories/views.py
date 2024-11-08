from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Category
from .serializers import CategorySerializer

def index(request):
    """
    Renders the index.html template.
    """
    return render(request, 'categories/index.html') 

class CategoryViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.validate_data.get('parent') == self.request.data.get('id'):
                raise serializer.ValidationError("Category cannot be its own parent.")
        serializer.save()
        return super().perform_create(serializer)


    def perform_update(self, serializer):
        """
        Override the update method to perform the validation before saving.
        """
        if serializer.validated_data.get('parent') == self.kwargs.get('pk'):
            raise serializer.ValidationError("Category cannot be its own parent.")
        serializer.save()