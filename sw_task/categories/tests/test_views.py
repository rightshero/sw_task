from django.test import TestCase
from django.urls import reverse
from .common import CommonUtils


class TestCategoriesViews(TestCase, CommonUtils):

    def setUp(self):
        self.num = 3
        self.categories, _ = self.create_categories(count=self.num)
    
    def test_home(self):
        response = self.client.get(reverse("categories-home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "categories/categories.html")
        self.assertEqual(len(response.context["categories"]), self.num)

