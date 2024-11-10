from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Category
from .serializers import CategorySerializer
from rest_framework import serializers

def index(request):
    """
    Renders the index.html template.
    """
    return render(request, 'index.html')

class CategoryViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if serializer.validated_data.get('parent') == self.request.data.get('parent'):
                raise serializers.ValidationError("Category cannot be its own parent.")
        serializer.save()
        return super().perform_update(serializer)

