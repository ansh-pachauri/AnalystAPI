from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from api.models import Customer, Product, Order, OrderItem
from api.serializers import CustomerSerializer, ProductSerializer, OrderSerializer, OrderItemSerializer
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models import Sum, F, DecimalField

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
            
            
@api_view(['GET'])
@permission_classes([AllowAny])
def sales_summary(request):
    total_sales = OrderItem.objects.aggregate( total=Sum(
            F('product__price') * F('quantity'),
            output_field=DecimalField(max_digits=10, decimal_places=2)
        ))['total'] or 0
    
    total_customers = Customer.objects.count()
    
    total_product_sold = OrderItem.objects.aggregate(total = Sum('quantity'))['total'] or 0
    
    return Response({
        "total_sales": float(total_sales),
        "total_customers": total_customers,
        "total_products_sold": total_product_sold
    })
    
    
@api_view(['GET'])
def top_customers(request):
    data = (
        OrderItem.objects.values('order__customer__id', 'order__customer__name')
        .annotate(total_spent=Sum(F('quantity') * F('product__price')))
        .order_by('-total_spent')[:5]
    )
    
    
    return Response(data)


@api_view(['GET'])
def top_products(request):
    data = (
        OrderItem.objects.values('product__id', 'product__name')
        .annotate(total_sold = Sum('quantity'))
        .order_by('-total_sold')[:5]
    )
    
    return Response(data)