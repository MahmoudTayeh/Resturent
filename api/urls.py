from rest_framework.routers import DefaultRouter
from api.views.meal_views import MealViewSet,MealOptionViewSet
from api.views.order_views import OrderViewSet
from api.views.user_views import DeliveryPersonViewSet,UserManagementViewSet
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

router = DefaultRouter()
router.register(r'meals', MealViewSet,basename='meal')
router.register(r'orders',OrderViewSet,basename='order')
router.register(r'meal-options', MealOptionViewSet,basename='meal-option')
router.register(r'delivery-personnel', DeliveryPersonViewSet)
router.register(r'users', UserManagementViewSet,basename='user')
urlpatterns = router.urls + [
               path('auth/', obtain_auth_token),
               ]

