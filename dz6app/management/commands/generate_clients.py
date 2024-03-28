import random
from django.core.management.base import BaseCommand
from dz6app.models import Client

class Command(BaseCommand):
    help = 'Generates and adds a specified number of clients to the database with predefined names and addresses'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='Number of clients to create')

    def handle(self, *args, **kwargs):
        number = kwargs['number']
        first_names = ['Иван', 'Алексей', 'Мария', 'Ольга', 'Сергей']
        last_names = ['Иванов', 'Петров', 'Сидорова', 'Кузнецова', 'Васильев']
        addresses = ['Москва, ул. Ленина, д.1', 'Санкт-Петербург, Невский пр., д.100', 'Новосибирск, ул. Мира, д.50',
                     'Екатеринбург, ул. Ленина, д.23', 'Казань, Кремлевская ул., д.12']

        for _ in range(number):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            address = random.choice(addresses)
            # Пример генерации полного имени
            full_name = f'{first_name} {last_name}'
            # Пример генерации электронной почты на основе имени
            email = f'{first_name.lower()}.{last_name.lower()}@example.com'
            # Простая генерация телефонного номера (здесь для примера)
            phone = (f'{random.randint(100, 999)}-{random.randint(100, 999)}-'
                     f'{random.randint(1000, 9999)}')

            client = Client(
                client=full_name,
                email=email,
                phone=phone,
                address=address
            )
            client.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully added client {client.client}'))