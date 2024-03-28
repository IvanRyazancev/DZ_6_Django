from django.core.management.base import BaseCommand
from dz6app.models import Client, Product, Order


class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        client = Client.objects.filter(id=id).first()
        self.stdout.write(f'{client}')