import uuid

from . import exceptions
from .models import Category


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
        return model.objects.filter(parent=None)

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

    def get_subcategories(self, parent_id: uuid.uuid4, values: tuple[str]) -> list[Category] | list[dict]:
        parent = self.get_category(parent_id)
        if values:
            return list(parent.subcategories.values(*values))
        return parent.subcategories.all()


    def create_category_name(self, parent_name: str, subcategory_number: int) -> str:
        prefix = "SUB "
        return f"{prefix}{parent_name}-{subcategory_number + 1}"

    def create_subcategory_names(self, parent_name: str, count: int) -> list[str]:
        return [
            self.create_category_name(parent_name, i - 1)
            for i in range(1, count + 1)
        ]

    def get_or_create_subcategories(self, parent_id: uuid.uuid4, validated_data: list[dict] | None = None, values: tuple[str] | None = None) -> list[Category]:
        subcategories = self.get_subcategories(parent_id, values)
        if len(subcategories) == 0:
            if not validated_data:
                validated_data = [
                    {"name": name}
                    for name in self.create_subcategory_names(self.get_category(parent_id).name, 2)
                ]
            subcategories = self.create_subcategories(parent_id, validated_data)
            return self.get_subcategories(parent_id, values)
        return subcategories
