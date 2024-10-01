import uuid
from .models import Category
from . import exceptions

class CategoriesService:
    model = Category

    def get_model(self) -> Category:
        return self.model 

    def create_categories(self, validated_data: list[dict]) -> list[Category]:
        categories = []
        model = self.get_model()
        for item in validated_data:
            # if category with this name already exists, skip it
            if model.objects.filter(name=item["name"]).exists():
                continue
            category = model.objects.create(**item)
            categories.append(category)
        return categories
    
    def get_category(self, category_id: uuid.uuid4) -> Category:
        model = self.get_model()
        try:
            return model.objects.get(id=category_id)
        except model.DoesNotExist:
            raise exceptions.CategoryNotFoundError from None

    def get_categories(self) -> list[Category]:
        model = self.get_model()
        return list(model.objects.all())

    def create_subcategories(self, parent_id: uuid.uuid4, validated_data: list[dict]) -> list[Category]:
        parent = self.get_category(parent_id)
        subcategories = []
        model = self.get_model()
        for item in validated_data:
            # if subcategory with this name already exists, skip it
            if model.objects.filter(name=item["name"]).exists():
                continue
            subcategory = model.objects.create(parent=parent, **item)
            subcategories.append(subcategory)
        return subcategories

    def get_subcategories(self, parent_id: uuid.uuid4) -> list[Category]:
        parent = self.get_category(parent_id)
        return list(parent.subcategories.all())