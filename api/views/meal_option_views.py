from rest_framework.viewsets import ModelViewSet
from api.permissions import IsAdminOrOwner
from management.models import MealOption
from api.serializers.meal_option_serializers import MealOptionDetailSerializer, MealOptionCreateUpdateSerializer

class MealOptionViewSet(ModelViewSet):
    queryset = MealOption.objects.all()
    permission_classes = [IsAdminOrOwner]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return MealOptionCreateUpdateSerializer
        return MealOptionDetailSerializer