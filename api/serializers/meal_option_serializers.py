from rest_framework import serializers
from management.models import MealOption

class MealOptionCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealOption
        fields = ['id', 'title', 'price_differences']
        
class MealOptionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealOption
        fields = ['id', 'meal', 'title', 'price_differences']