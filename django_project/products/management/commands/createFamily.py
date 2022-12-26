from django.core.management.base import BaseCommand
from products.models import Family

class Command(BaseCommand):
    def handle(self, *args, **options):
        Family.objects.create(name='Christian', age=35, relationship='Hermano mayor', alive=True)
        Family.objects.create(name='Lautaro', age=17, relationship='Hermano menor', alive=True)
        Family.objects.create(name='Carmen', age=59, relationship='Madre', alive=True)
        Family.objects.create(name='Adriana', age=24, relationship='Esposa', alive=True)
        Family.objects.create(name='Susi', age=5, relationship='Perra', alive=True)
        Family.objects.create(name='Mora', age=1, relationship='Perra', alive=True)

        