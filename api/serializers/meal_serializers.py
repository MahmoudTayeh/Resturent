from rest_framework import serializers 
from management.models import Meal, MealOption

class MealOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealOption
        fields = ['id', 'title', 'price_differences']

class MealSerializer(serializers.ModelSerializer):
    options = MealOptionSerializer(many=True , read_only=True)
    
    class Meta:
        model = Meal
        fields = ['id', 'name', 'description', 'price', 'image', 'options']
