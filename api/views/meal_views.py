from rest_framework.viewsets import ModelViewSet
from api.permissions import IsAdminOrOwner
from management.models import Meal,MealOption
from api.serializers.meal_serializers import MealSerializer,MealOptionSerializer
from api.serializers.meal_option_serializers import MealOptionCreateUpdateSerializer,MealOptionDetailSerializer

class MealViewSet(ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAdminOrOwner]

class MealOptionViewSet(ModelViewSet):
    queryset = MealOption.objects.all()
    serializer_class = MealOptionSerializer
    permission_classes = [IsAdminOrOwner]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return MealOptionCreateUpdateSerializer
        return MealOptionDetailSerializer
