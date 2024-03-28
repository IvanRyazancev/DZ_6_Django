from django.core.management.base import BaseCommand
from dz6app.models import Product
from decimal import Decimal

class Command(BaseCommand):
    help = 'Добавляет новый продукт'

    def add_arguments(self, parser):
        parser.add_argument('product_name', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('price', type=Decimal)
        parser.add_argument('quantity', type=int)

    def handle(self, *args, **options):
        product = Product(
            product=options['product_name'],
            description=options['description'],
            price=options['price'],
            quantity=options['quantity']
        )
        product.save()
        self.stdout.write(self.style.SUCCESS(f'Successfully added product "{product.product}" with ID {product.id}'))
