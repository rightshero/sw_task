from sw_task.categories.services import CategoriesService

class CommonUtils:
    categories_service = CategoriesService()
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