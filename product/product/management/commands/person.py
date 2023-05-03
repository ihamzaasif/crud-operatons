from django.core.management.base import BaseCommand, CommandError
from product.models import Product

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('name')
        parser.add_argument('color')
        parser.add_argument('price', type=int, help='Please enter price in the integer form')
        
    def handle(self, *args, **options):
        person = Product(
            name=options['name'],
            color=options['color'],
            price=options['price']
        )
        person.save()
        self.stdout.write(self.style.SUCCESS('Added Member!'))