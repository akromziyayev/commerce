from django.contrib import admin
from django.urls import path, include
from app.views import index, product_detail, add_product
from customer.views import customers, add_customer, delete_customers,edit_customer

urlpatterns = [
    path('customer-list', customers, name='customers'),
    path('add-customer/', add_customer, name='add_customer'),
    path('delete-customer/<int:pk>/delete',delete_customers, name='delete'),
    path('customer/<int:pk>/update',edit_customer, name='edit')
]

