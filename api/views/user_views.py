from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from api.permissions import IsOwner
from accounts.models import CustomUser
from api.serializers.user_serializers import DeliveryPersonSerializer, UserListSerializer

class DeliveryPersonViewSet(ModelViewSet):
    queryset = CustomUser.objects.filter(is_delivery=True)
    serializer_class = DeliveryPersonSerializer
    permission_classes = [IsOwner]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_active']
    search_fields = ['name', 'phone_number', 'email']
    ordering_fields = ['created_at', 'name']
    
    @action(detail=True, methods=['patch'], permission_classes=[IsOwner])
    def toggle_active(self, request, pk=None):
        """Toggle active status of delivery person"""
        delivery_person = self.get_object()
        delivery_person.is_active = not delivery_person.is_active
        delivery_person.save()
        
        serializer = self.get_serializer(delivery_person)
        return Response(serializer.data)

class UserManagementViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsOwner]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_owner', 'is_delivery', 'is_staff', 'is_active']
    search_fields = ['name', 'phone_number', 'email']
    ordering_fields = ['created_at', 'name']
    
    @action(detail=True, methods=['patch'], permission_classes=[IsOwner])
    def make_delivery_person(self, request, pk=None):
        """Make a user a delivery person"""
        user = self.get_object()
        if user.is_delivery :
            return Response({"detail" : "User is already a delivery person"}, status=400)
        user.is_delivery = True
        user.save()
        
        serializer = self.get_serializer(user)
        return Response(serializer.data)
    
    @action(detail=True, methods=['patch'], permission_classes=[IsOwner])
    def remove_delivery_role(self, request, pk=None):
        """Remove delivery role from a user"""
        user = self.get_object()
        if not user.is_delivery :
            return Response({"detaile": "User is not a delivery person."},status=400)
        user.is_delivery = False
        user.save()
        
        serializer = self.get_serializer(user)
        return Response(serializer.data)
    