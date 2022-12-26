from django.core.management.base import BaseCommand
from products.models import Family

class Command(BaseCommand):
    def handle(self, *args, **options):
        Family.objects.create(name='Christian', age=35, relationship='Brother', alive=True)
        Family.objects.create(name='Lautaro', age=17, relationship='Sister', alive=True)
        Family.objects.create(name='Carlos', age=65, relationship='Father', alive=False)
        Family.objects.create(name='Carmen', age=59, relationship='Mother', alive=True)