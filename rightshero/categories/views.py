from rest_framework import viewsets ,response,status
from .models import Category
from rest_framework.response import Response
from rest_framework.decorators import action 
from .serializers import CategorySerializer
from utils.utils import custom_response 

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    @action(detail=False, methods=['get'])
    #all_categories
    def all_categories(self, request):
        parent_categories = Category.objects.filter(parent=None)
        categories_data = [self.get_category_with_children(parent) for parent in parent_categories]
        # return Response(categories_data)
        return  custom_response(data=categories_data, message="Data fetched successfully", code=200)
    
    def get_category_with_children(self, category):
        """Recursively get category and its children."""
        children = category.subcategories.all()
        return {
            "id": category.id,
            "name": category.name,
            "children": [self.get_category_with_children(child) for child in children]
        }

    def retrieve(self, request, *args, **kwargs):
        """Override retrieve method to return category with children."""
        instance = self.get_object()
        data = self.get_category_with_children(instance)
        # return response.Response(data)
        return custom_response(data= data,  message="Data fetched successfully", code=200)
    
    def create(self, request, *args, **kwargs):
        """Override create method to return the root category along with its entire hierarchy."""
        
        # Ensure that the request's content type is application/json
        if not request.content_type == 'application/json':
            return custom_response(data=None,message= 'Invalid content type. Expected application/json', code=400)
    
        # Check if the required fields are present in the request
        if 'name' not in request.data or 'parent' not in request.data:
            return custom_response(data=None, message="Both 'name' and 'parent' fields are required.", code=400)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            category = serializer.save()

            # # Find the root category (the top-most parent)
            # root_category = category
            # while root_category.parent is not None:
            #     root_category = root_category.parent

            # # Fetch the entire tree from the root category
            # category_hierarchy = self.get_category_with_children(root_category)
            custom_response_data = {
            'id': category.id,
            'name': category.name,
            'children':[]
            }

            # Return the hierarchy starting from the root category
            return custom_response(data=custom_response_data, message="Category created successfully", code=200)

        return custom_response(data=None, message= "Incorrect Value in Parent or Category", code=status.HTTP_400_BAD_REQUEST)


