from django.core.management.base import BaseCommand
from dz6app.models import Order


class Command(BaseCommand):
    help = "Delete user by id."
    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='User ID')
    def handle(self, *args, **kwargs):
        id = kwargs.get('id')
        order = Order.objects.filter(id=id).first()
        if order is not None:
            order.delete()
            self.stdout.write(f'{order}')