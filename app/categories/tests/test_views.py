from django.test import TestCase
from django.urls import reverse

from app.categories.models import Category


class CategoryViewsTestCase(TestCase):

    def setUp(self):
        """
        Setup method to create initial test data.
        """
        # Create some categories for testing
        self.category_a = Category.objects.create(name='Category A')
        self.category_b = Category.objects.create(name='Category B')

    def test_index_view(self):
        """
        Test the IndexView to ensure it fetches and renders the root categories.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories/index.html')
        self.assertContains(response, 'Category A')
        self.assertContains(response, 'Category B')

    def test_create_category_view(self):
        """
        Test the CreateCategoryView to ensure it creates a new root category.
        """
        response = self.client.post(reverse('create_category'), {
            'name': 'Category C'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Category.objects.filter(name='Category C').exists())

        # Test creation of a subcategory
        response = self.client.post(reverse('create_category'), {
            'name': 'Sub Category A1',
            'parent_id': self.category_a.id
        })
        self.assertEqual(response.status_code, 200)
        sub_category = Category.objects.get(name='Sub Category A1')
        self.assertEqual(sub_category.parent, self.category_a)

    def test_create_subcategory_view(self):
        """
        Test the CreateSubCategoryView to ensure it creates subcategories for a given parent.
        """
        response = self.client.post(reverse('create_subcategory'), {
            'parent_id': self.category_b.id
        })
        self.assertEqual(response.status_code, 200)
        subcategories = Category.objects.filter(parent=self.category_b)
        self.assertEqual(subcategories.count(), 2)
        self.assertTrue(Category.objects.filter(name=f'SUB {self.category_b.name}1').exists())
        self.assertTrue(Category.objects.filter(name=f'SUB {self.category_b.name}2').exists())

    def test_remove_subcategory_view(self):
        """
        Test the RemoveSubCategoryView to ensure it removes all subcategories for a given parent.
        """
        # First, create some subcategories under Category B
        sub_category_b1 = Category.objects.create(name=f'SUB {self.category_b.name}1', parent=self.category_b)
        sub_category_b2 = Category.objects.create(name=f'SUB {self.category_b.name}2', parent=self.category_b)

        # Now test removing them
        response = self.client.post(reverse('remove_subcategory'), {
            'parent_id': self.category_b.id
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Category.objects.filter(parent=self.category_b).exists())
