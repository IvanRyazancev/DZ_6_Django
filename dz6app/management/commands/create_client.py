from django.core.management.base import BaseCommand
from dz6app.models import Client

class Command(BaseCommand):
    help = 'Добавляет нового клиента'

    def add_arguments(self, parser):
        parser.add_argument('client_name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('phone', type=str)
        parser.add_argument('address', type=str)

    def handle(self, *args, **options):
        client = Client(
            client=options['client_name'],
            email=options['email'],
            phone=options['phone'],
            address=options['address']
        )
        client.save()
        self.stdout.write(self.style.SUCCESS(f'Successfully added client "{client.client}" with ID {client.id}'))