from django.core.management.base import BaseCommand
from dz6app.models import Client


class Command(BaseCommand):
    help = "Get all users."

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        if clients:
            for client in clients:
                self.stdout.write(f'ID: {client.id}, Название: {client.client}, Цена: {client.email}, '
                                  f'Количество: {client.phone}, Адрес: {client.address}, Дата регистрации: '
                                  f'{client.date_registered}')
        else:
            self.stdout.write(self.style.WARNING('Нет доступных клиентов.'))