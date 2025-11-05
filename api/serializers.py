from rest_framework import serializers
from api.models import Customer, Product, Order, OrderItem

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model =Customer
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields = '__all__'

        
class OrderItemSerializer(serializers.ModelSerializer):
       product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

       class Meta:
        model = OrderItem
        fields = ['product', 'quantity']       
        
        
        
        
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
     
    class Meta:
        model =Order
        fields = ['id', 'customer', 'order_date', 'items']
        read_only_fields = ['order_date']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
                