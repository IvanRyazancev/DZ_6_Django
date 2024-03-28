from django.core.management.base import BaseCommand
from dz6app.models import Client, Product, Order, OrderItem


class Command(BaseCommand):
    help = 'Создаёт заказ для клиента и рассчитывает общую стоимость заказа'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int)
        parser.add_argument('product_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        client_id = options['client_id']
        product_ids = options['product_ids']

        # Проверяем существование клиента
        try:
            client = Client.objects.get(pk=client_id)
        except Client.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Client with ID "{client_id}" does not exist.'))
            return

        # Создаем заказ
        order = Order(client=client)
        order.save()

        # Добавляем продукты в заказ и рассчитываем total_price
        total_price = 0
        for product_id in product_ids:
            try:
                product = Product.objects.get(pk=product_id)
                order_item = OrderItem(order=order, product=product, quantity=1)  # Предполагаем quantity=1 для примера
                order_item.save()
                total_price += product.price  # Добавляем цену продукта к общей стоимости
            except Product.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Product with ID "{product_id}" does not exist. Skipping.'))
                continue

        # Обновляем и сохраняем общую стоимость заказа
        order.total_price = total_price
        order.save()

        self.stdout.write(self.style.SUCCESS(
            f'Successfully created order with ID {order.id} for client "{client.client}". Total price: {total_price}'))