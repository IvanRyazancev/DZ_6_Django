from itertools import product

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from djangoProject import settings
from dz6app import views

app_name = 'dz6app'

urlpatterns = [
    path('clients/', views.client_list, name='clients'),
    path('products/', views.product_list, name='products'),
    path('orders/', views.orders_list, name='orders'),
    path('add_product/', views.add_product, name='add_product'),
    # path('__debug__/', include("debug_toolbar.urls")),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('create-order/', views.create_order, name='create_order'),
    path('order/<int:product_id>/', views.order_page, name='order_page'),
]