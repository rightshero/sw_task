from django.apps import AppConfig


class CategoriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'categories'
    def ready(self):
        from .initial_data import create_initial_categories # type: ignore
        create_initial_categories()