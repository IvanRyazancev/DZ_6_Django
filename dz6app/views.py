from datetime import timezone, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect

from dz6app.forms import ProductForm
from .models import Product, Order, Client, OrderItem
from datetime import timedelta
from django.utils import timezone
from django.contrib import messages


# Create your views here.
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('save-success')  # Перенаправление после сохранения
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})


def view_name(request):
    return render(request, 'success.html')


def save_success(request):
    return render(request, 'success.html')


def unique_products_from_orders(orders):
    unique_products = set()
    for order in orders:
        for item in order.orderitem_set.all():
            unique_products.add(item.product)
    return unique_products


def client_orders(request, client_id):
    now = timezone.now()
    client_orders_last_7_days = Order.objects.filter(client_id=client_id, date_ordered__gte=now - timedelta(days=7))
    client_orders_last_month = Order.objects.filter(client_id=client_id, date_ordered__gte=now - timedelta(days=30))
    client_orders_last_year = Order.objects.filter(client_id=client_id, date_ordered__gte=now - timedelta(days=365))

    products_last_7_days = unique_products_from_orders(client_orders_last_7_days)
    products_last_month = unique_products_from_orders(client_orders_last_month)
    products_last_year = unique_products_from_orders(client_orders_last_year)

    context = {
        'products_last_7_days': products_last_7_days,
        'products_last_month': products_last_month,
        'products_last_year': products_last_year,
    }

    return render(request, 'client_products.html', context)


def my_page(request):
    return render(request, 'my_page.html')


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})


def product_list(request):
    sort = request.GET.get('sort', 'id')
    if sort == 'price':
        products = Product.objects.all().order_by('price')
    elif sort == 'name':
        products = Product.objects.all().order_by('product')
    else:
        products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def orders_list(request):
    orders = Order.objects.select_related('client').prefetch_related('products').all()
    return render(request, 'orders.html', {'orders': orders})


def total_in_template(request):
    context = {
        'title': 'Общее количество посчитано в шаблоне',
        'products': Product,
    }
    return render(request, 'total_count.html', context)


@require_http_methods(["POST"])
def subscribe(request):
    email = request.POST.get('email', '')
    return HttpResponse(f"Спасибо за подписку, ваш email: {email} получен!")


def create_order(request):
    if request.method == 'POST':
        # Получаем данные из формы
        client_name = request.POST.get('client')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        product_id = request.POST.get('product_id')

        client = Client(client=client_name, email=email, phone=phone, address=address)
        client.save()

        order = Order(client=client)
        order.save()

        product = Product.objects.get(id=product_id)
        order_item = OrderItem(product=product, order=order,
                               quantity=1)  # Предполагается, что заказывается 1 единица товара
        order_item.save()

        order.update_total_price()

        messages.success(request, 'Заказ успешно создан!'),
        return render(request, 'order_confirmation.html', {'product_id': product_id})

    return redirect('/')

def order_page(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'order_form.html', {'product': product})