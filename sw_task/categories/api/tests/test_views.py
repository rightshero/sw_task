from django.test import TestCase
from django.urls import reverse

from sw_task.categories.services import CategoriesService


class TestCategoryAPIView(TestCase):

    def setUp(self):
        self.categories_service = CategoriesService()
        self.num = 3
        self.categories, _ = self.create_categories(count=self.num)
        self.subcategories, _ = self.create_subcategories(self.categories[0].id, count=self.num)

    def create_categories(self, count=3):
        data = [
            {"name": f"Category {i}"}
            for i in range(1, count + 1)
        ]
        created_categories = self.categories_service.create_categories(
            data
        )
        return created_categories, data
    
    def create_subcategories(self, parent_id, count=3):
        data = [
            {"name": f"Subcategory {i}"} for i in range(1, count + 1)
        ]
        created_subcategories = self.categories_service.create_subcategories(
            parent_id, data
        )
        return created_subcategories, data
   
    def test_subcategories_list(self):
        response = self.client.get(reverse('subcategories-list', kwargs={'category_id': self.categories[0].id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), self.num)

    def test_subcategories_list_method_not_allowed(self):
        response = self.client.post(reverse('subcategories-list', kwargs={'category_id': self.categories[0].id}))
        self.assertEqual(response.status_code, 405)