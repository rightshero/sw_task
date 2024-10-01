from django.test import TestCase
from sw_task.categories.services import CategoriesService
from sw_task.categories import exceptions
from .common import CommonUtils


class TestCategories(TestCase, CommonUtils):

    def test_create_categories(self):
        count = 3
        created_categories, data_input = self.create_categories(count=count)
        for i, category in enumerate(created_categories):
            self.assertEqual(category.name, data_input[i]["name"])
    
    def test_create_categories_with_existing_categories(self):
        count = 3
        created_categories, data_input = self.create_categories(count=count)
        self.assertEqual(len(created_categories), count)
        created_categories, data_input = self.create_categories(count=count)
        self.assertEqual(len(created_categories), 0)
        created_categories, data_input = self.create_categories(count=count + 1)
        self.assertEqual(len(created_categories), 1)
        

    def test_get_category(self):
        created_categories, data_input = self.create_categories(count=1)
        category = self.categories_service.get_category(created_categories[0].id)
        self.assertEqual(category.name, data_input[0]["name"])

    def test_get_category_not_found(self):
        with self.assertRaises(exceptions.CategoryNotFoundError):
            self.categories_service.get_category(0)

    def test_get_categories(self):
        self.assertEqual(len(self.categories_service.get_categories()), 0)
        count = 3
        created_categories, _ = self.create_categories(count=count)
        categories = self.categories_service.get_categories()
        self.assertEqual(len(categories), count)

    def test_create_subcategories(self):
        count = 1
        created_categories, _ = self.create_categories(count=count)
        parent_category = created_categories[0]
        created_subcategories, data_input = self.create_subcategories(
            parent_category.id, count=count + 1
        )
        self.assertEqual(len(created_subcategories), count + 1)
        for i, subcategory in enumerate(created_subcategories):
            self.assertEqual(subcategory.name, data_input[i]["name"])
            self.assertEqual(subcategory.parent, parent_category)

    def test_create_subcategories_parent_not_found(self):
        with self.assertRaises(exceptions.CategoryNotFoundError):
            self.create_subcategories(0)
    
    def test_create_subcategories_with_existing_subcategories(self):
        count = 1
        created_categories, _ = self.create_categories(count=count)
        parent_category = created_categories[0]
        created_subcategories, data_input = self.create_subcategories(
            parent_category.id, count=count
        )
        self.assertEqual(len(created_subcategories), count)
        created_subcategories, data_input = self.create_subcategories(
            parent_category.id, count=count
        )
        self.assertEqual(len(created_subcategories), 0)
        created_subcategories, data_input = self.create_subcategories(
            parent_category.id, count=count + 1
        )
        self.assertEqual(len(created_subcategories), 1)
        self.assertEqual(created_subcategories[0].name, data_input[-1]["name"])
        self.assertEqual(created_subcategories[0].parent, parent_category)

    def test_get_subcategories(self):
        count = 1
        created_categories, _ = self.create_categories(count=count)
        parent_category = created_categories[0]
        self.assertEqual(len(parent_category.subcategories.all()), 0)
        count = 3
        created_subcategories, _ = self.create_subcategories(
            parent_category.id, count=count
        )
        self.assertEqual(len(parent_category.subcategories.all()), count)
        subcategories = self.categories_service.get_subcategories(parent_category.id)
        self.assertEqual(len(subcategories), count)
        for i, subcategory in enumerate(subcategories):
            self.assertEqual(subcategory.name, f"Subcategory {i + 1}")
            self.assertEqual(subcategory.parent, parent_category)

    def test_get_subcategories_parent_not_found(self):
        with self.assertRaises(exceptions.CategoryNotFoundError):
            self.categories_service.get_subcategories(0)
    
    def test_get_subcategories_with_specific_fields_only(self):
        count = 1
        created_categories, _ = self.create_categories(count=count)
        parent_category = created_categories[0]
        self.assertEqual(len(parent_category.subcategories.all()), 0)
        count = 3
        created_subcategories, _ = self.create_subcategories(
            parent_category.id, count=count
        )
        self.assertEqual(len(parent_category.subcategories.all()), count)
        subcategories = self.categories_service.get_subcategories(
            parent_category.id, values=("name",)
        )
        self.assertEqual(len(subcategories), count)
        for i, subcategory in enumerate(subcategories):
            self.assertEqual(subcategory["name"], f"Subcategory {i + 1}")
            self.assertNotIn("parent", subcategory)
