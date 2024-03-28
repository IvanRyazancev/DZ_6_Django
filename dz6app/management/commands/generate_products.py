from django.core.management.base import BaseCommand
from faker import Faker
from dz6app.models import Product
import random

class Command(BaseCommand):
    help = 'Creates a specified number of fake products'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='The number of fake products to create')

    def handle(self, *args, **kwargs):
        number = kwargs['number']
        fake = Faker()
        products_to_create = []
        for _ in range(number):
            product = Product(
                product=fake.catch_phrase(),
                description=fake.text(max_nb_chars=200),
                price=round(random.uniform(10.0, 1000.0), 2),
                quantity=random.randint(1, 100),
                photo=None)
            products_to_create.append(product)

            self.stdout.write(self.style.SUCCESS(f'Successfully created product: {product.product}'))

        Product.objects.bulk_create(products_to_create)