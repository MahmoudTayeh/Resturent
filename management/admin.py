from django.contrib import admin
from .models import Order,OrderItem,Meal,MealOption
# Register your models here.

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Meal)
admin.site.register(MealOption)
