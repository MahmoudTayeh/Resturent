from rest_framework import serializers
from accounts.models import CustomUser

class DeliveryPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'phone_number', 'name', 'email', 'address', 'is_delivery', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']
    
    def create(self, validated_data):
        validated_data['is_delivery'] = True
        user = CustomUser.objects.create_user(**validated_data)
        return user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'phone_number', 'name', 'email', 'is_owner', 'is_delivery', 'is_staff', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']