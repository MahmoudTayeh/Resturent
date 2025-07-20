from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from api.permissions import IsAdminOrOwner, IsOwner
from management.models import Order,OrderItem
from api.serializers.order_serializers import OrderSerializer
from accounts.models import CustomUser
from django.db.models import Count, Sum, F, ExpressionWrapper, DecimalField
from django.utils import timezone
from datetime import timedelta

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
    permission_classes = [IsOwner]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'created_at']
    search_fields = ['user__name', 'user__phone_number', 'unique_order_code']
    ordering_fields = ['created_at', 'total_price', 'status']
    
    def get_queryset(self):
        # Optionally, filter by owner logic if needed later
        return super().get_queryset()

    def update_status(self, serializer):
        order = self.get_object()
        
        serializer.save()
    
    @action(detail=True, methods=['patch'], permission_classes=[IsOwner])
    def assign_delivery(self, request, pk=None):
        """Assign a delivery person to an order"""
        order = self.get_object()
        delivery_person_id = request.data.get('delivery_person_id')
        
        if not delivery_person_id:
            return Response(
                {'error': 'delivery_person_id is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            delivery_person = CustomUser.objects.get(
                id=delivery_person_id, 
                is_delivery=True
            )
            order.contact_phone = delivery_person
            order.save()
            
            serializer = self.get_serializer(order)
            return Response(serializer.data)
        except CustomUser.DoesNotExist:
            return Response(
                {'error': 'Delivery person not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=False, methods=['get'], permission_classes=[IsOwner])
    def statistics(self, request):
        """Get order statistics for the owner dashboard"""
        today = timezone.now().date()
        week_ago = today - timedelta(days=7)
        month_ago = today - timedelta(days=30)
        most_ordered_meals = (
        OrderItem.objects
        .values('meal_name')
        .annotate(total_quantity=Sum('quantity'))
        .order_by('-total_quantity')[:5]  # أفضل 5 فقط
    )

        # الوجبات الأعلى دخلًا
        total_income_expr = ExpressionWrapper(
            F('unit_price') * F('quantity'),
            output_field=DecimalField(max_digits=10, decimal_places=2)
        )

        top_income_meals = (
            OrderItem.objects
            .annotate(total_income=total_income_expr)
            .values('meal_name')
            .annotate(income=Sum('total_income'))
            .order_by('-income')[:5]
        )

        stats = {
            'total_orders': Order.objects.count(),
            'today_orders': Order.objects.filter(created_at__date=today).count(),
            'week_orders': Order.objects.filter(created_at__date__gte=week_ago).count(),
            'month_orders': Order.objects.filter(created_at__date__gte=month_ago).count(),
            'total_revenue': Order.objects.aggregate(Sum('total_price'))['total_price__sum'] or 0,
            'today_revenue': Order.objects.filter(created_at__date=today).aggregate(Sum('total_price'))['total_price__sum'] or 0,
            'orders_by_status': Order.objects.values('status').annotate(count=Count('id')),
            'top_selling_meals':most_ordered_meals,
            'top_income_meals':top_income_meals,
        }
        
        return Response(stats)