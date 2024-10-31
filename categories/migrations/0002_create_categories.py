from django.db import migrations
from ..models import Category

def add_category(apps, schema_editor):
    # Check if the table is empty
    if Category.objects.exists():
        return
    # Create initial categories
    Category.objects.create(name='Category A')
    Category.objects.create(name='Category B')

class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_category),
    ]
