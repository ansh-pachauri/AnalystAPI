from django.db import models

# Create your models here.
class Customer(models.Model):
    id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    joined_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order #{self.id}"
    
class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    
    def __str__(self):
        return f"{self.product.name} x {self.quantity}"