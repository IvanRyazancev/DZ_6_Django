from django.core.management.base import BaseCommand, CommandError
from dz6app.models import Client

class Command(BaseCommand):
    help = 'Обновляет имя продукта по его ID'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int)
        parser.add_argument('new_name', type=str)

    def handle(self, *args, **options):
        client_id = options['client_id']
        new_name = options['new_name']

        try:
            client = Client.objects.get(id=client_id)
            client.client = new_name
            client.save()
            self.stdout.write(self.style.SUCCESS(f'Product with id "{client_id}" has been updated with new name '
                                                 f'"{new_name}".'))
        except Client.DoesNotExist:
            raise CommandError(f'Product with id "{client_id}" does not exist.')