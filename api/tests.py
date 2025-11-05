from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Customer, Product, Order, OrderItem
from decimal import Decimal

class SalesSummaryTest(TestCase):
    def setUp(self):
        
        self.client = APIClient()
        
        
        self.customer = Customer.objects.create(
            name="Test Customer",
            email="test@example.com"
        )
        
        # Create products
        self.product1 = Product.objects.create(
            name="Product 1",
            price=Decimal('10.00')
        )
        self.product2 = Product.objects.create(
            name="Product 2",
            price=Decimal('20.00')
        )
        
        # Create an order
        self.order = Order.objects.create(customer=self.customer)
        
        # Create order items
        OrderItem.objects.create(
            order=self.order,
            product=self.product1,
            quantity=2 
        )
        OrderItem.objects.create(
            order=self.order,
            product=self.product2,
            quantity=1 
        )

    def test_sales_summary(self):
        # Get the sales summary
        url = reverse('sales-summary')
        response = self.client.get(url)
        
        # Check if response is successful
        self.assertEqual(response.status_code, 200)
        
        # Check the response data
        self.assertEqual(response.data['total_sales'], 40.0) 
        self.assertEqual(response.data['total_customers'], 1)
        self.assertEqual(response.data['total_products_sold'], 3)  
        
    def test_empty_sales_summary(self):
        # Delete all orders
        Order.objects.all().delete()
        
        # Get the sales summary
        url = reverse('sales-summary')
        response = self.client.get(url)
        
        
        self.assertEqual(response.status_code, 200)
        
        # Check the response data for empty state
        self.assertEqual(response.data['total_sales'], 0)
        self.assertEqual(response.data['total_customers'], 1)  
        self.assertEqual(response.data['total_products_sold'], 0)
