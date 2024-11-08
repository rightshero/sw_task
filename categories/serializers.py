from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):

    """Serializer for the Category model."""
    class Meta:
        model = Category
        
        fields = ['id', 'name', 'parent']

    def update(self, instance, validated_data):
        if validated_data.get("parent").id == instance.id:
            raise serializers.ValidationError("Category cannot be its own parent.")
        return super().update(instance, validated_data)