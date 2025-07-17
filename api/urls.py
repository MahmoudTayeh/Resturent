from rest_framework.routers import DefaultRouter
from api.views.meal_views import MealViewSet
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

router = DefaultRouter()
router.register(r'meals', MealViewSet,basename='meal')
urlpatterns = router.urls + [
               path('auth/', obtain_auth_token),
               ]

    