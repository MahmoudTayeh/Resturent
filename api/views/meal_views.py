from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.permissions import IsAdminOrOwner
from management.models import Meal
from api.serializers.meal_serializers import MealSerializer

class MealViewSet(ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAdminOrOwner]