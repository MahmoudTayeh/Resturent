from rest_framework import serializers
from management.models import Order,OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'created_at',
            'total_price',
            'status',
            'contact_phone',
            'items'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'items']
