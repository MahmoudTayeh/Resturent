from rest_framework import serializers
from management.models import Order,OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    user_name = serializers.CharField(source='user.name', read_only=True)
    user_address = serializers.CharField(source='user.address', read_only=True)
    class Meta:
        model = Order
        fields = [
            'id',
            'user_name',
            'user_address',
            'created_at',
            'total_price',
            'status',
            'contact_phone',
            'items'
        ]
        read_only_fields = ['id', 'user_name', 'created_at', 'items','user_address',]
