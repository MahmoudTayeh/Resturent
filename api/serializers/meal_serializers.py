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

    def create(self, validated_data):
        options_data = validated_data.pop('options', [])
        meal = Meal.objects.create(**validated_data)
        
        for option_data in options_data:
            MealOption.objects.create(meal=meal, **option_data)
        
        return meal
    
    def update(self, instance, validated_data):
        options_data = validated_data.pop('options', [])
        
        # Update meal fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        # Handle options update
        if options_data:
            # Delete existing options and create new ones
            instance.options.all().delete()
            for option_data in options_data:
                MealOption.objects.create(meal=instance, **option_data)
        
        return instance