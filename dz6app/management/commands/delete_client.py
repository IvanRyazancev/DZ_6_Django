from django.core.management.base import BaseCommand
from dz6app.models import Client


class Command(BaseCommand):
    help = "Delete user by id."
    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='User ID')
    def handle(self, *args, **kwargs):
        id = kwargs.get('id')
        client = Client.objects.filter(id=id).first()
        if client is not None:
            client.delete()
        self.stdout.write(f'{client}')