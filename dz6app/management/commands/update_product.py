from django.core.management.base import BaseCommand, CommandError
from dz6app.models import Product

class Command(BaseCommand):
    help = 'Обновляет имя продукта по его ID'

    def add_arguments(self, parser):
        parser.add_argument('product_id', type=int)
        parser.add_argument('new_name', type=str)

    def handle(self, *args, **options):
        product_id = options['product_id']
        new_name = options['new_name']

        try:
            product = Product.objects.get(id=product_id)
            product.product = new_name
            product.save()
            self.stdout.write(self.style.SUCCESS(f'Product with id "{product_id}" has been updated with '
                                                 f'new name "{new_name}".'))
        except Product.DoesNotExist:
            raise CommandError(f'Product with id "{product_id}" does not exist.')