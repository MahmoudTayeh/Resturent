from django.db import models
from django.conf import settings

# Create your models here.

class Meal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='meals/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class MealOption(models.Model):
    meal = models.ForeignKey(Meal,on_delete=models.CASCADE,related_name='options')
    title = models.CharField(max_length=100)
    price_differences = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.meal.name} -> {self.title}"

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart of {self.user.name}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE, related_name='items')
    meal = models.ForeignKey(Meal,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    option = models.ForeignKey(MealOption, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.quantity} x {self.meal.name} "

class Order(models.Model):
    STATUS_CHOICES = [
        ('preparing', 'Preparing'),
        ('ready', 'Ready'),
        ('on_the_way', 'On_the_way'),
        ('delivered', 'Delivered'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES,default='preparing')
    contact_phone = models.CharField(max_length=100)
    def __str__(self):
        return f"Order {self.id} by {self.user.name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    meal = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True)
    meal_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    option_title = models.CharField(max_length=100, blank=True, null=True)
    option_price_difference = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.quantity} x {self.meal_name}"