from rest_framework import serializers
from management.models import Cart, CartItem
from api.serializers.meal_serializers import MealSerializer,MealOptionSerializer

class CartItemSerializer(serializers.ModelSerializer):
    meal = MealSerializer(read_only=True)
    option = MealOptionSerializer(read_only=True)
    
    class Meta:
        model = CartItem
        fields = ['id', 'meal', 'quantity', 'option']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']