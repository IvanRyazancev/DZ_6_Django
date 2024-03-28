from django.contrib import admin
from dz6app.models import Client, Product, Order, OrderItem


# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client', 'email', 'phone', 'address', 'date_registered')  # Это поля,
    # которые будут отображаться в списке
    search_fields = ('client', 'email')  # Поля, по которым можно проводить поиск

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'quantity', 'date_added')
    search_fields = ('product',)
    list_filter = ('date_added',)  # Фильтры для удобства поиска

class OrderItemInline(admin.TabularInline):  # Используется для отображения inline в OrderAdmin
    model = OrderItem
    extra = 1  # Количество дополнительных форм для новых записей

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'date_ordered', 'total_price')
    inlines = (OrderItemInline,)  # Включение OrderItem в интерфейс Order
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)