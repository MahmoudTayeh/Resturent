from django.core.management.base import BaseCommand
from management.models import Meal,MealOption,Order,OrderItem
from accounts.models import CustomUser

class Command(BaseCommand):
    help = 'Seed the database with meals, options, and users'
    
    def handle(self, *args, **kwargs):
        
        #MealOption.objects.all().delete()
        #Meal.objects.all().delete()
        #CustomUser.objects.all().delete()
        Order.objects.all().delete()
        OrderItem.objects.all().delete()
    
        # Create Meals
        '''pizza = Meal.objects.create(name='Pizza', description='Cheesy pizza with toppings', price=30)
        burger = Meal.objects.create(name='Burger', description='Juicy beef burger', price=25)
        pasta = Meal.objects.create(name='Pasta', description='Creamy white sauce pasta', price=28)

        # Options for Pizza
        MealOption.objects.create(meal=pizza, title='Extra Cheese', price_differences=5)
        MealOption.objects.create(meal=pizza, title='No Olives', price_differences=0)

        # Options for Burger
        MealOption.objects.create(meal=burger, title='Double Patty', price_differences=7)
        MealOption.objects.create(meal=burger, title='Add Bacon', price_differences=4)

        # Options for Pasta
        MealOption.objects.create(meal=pasta, title='Add Chicken', price_differences=6)
        MealOption.objects.create(meal=pasta, title='Spicy Sauce', price_differences=2)

        # Create Users
        CustomUser.objects.create_user(
            name='Mona Admin',
            email='admin@example.com',
            phone_number='0591234567',
            address='Gaza City',
            password='adminpass',
            is_owner=True
        )

        CustomUser.objects.create_user(
            name='Tariq Delivery',
            email='delivery@example.com',
            phone_number='0597654321',
            address='Rafah',
            password='deliverypass',
            is_delivery=True
        )

        CustomUser.objects.create_user(
            name='Layla User',
            email='layla@example.com',
            phone_number='0595555555',
            address='Khan Younis',
            password='userpass'
        )'''
        admin_user = CustomUser.objects.get(phone_number='0591234567')
        regular_user = CustomUser.objects.get(phone_number='0595555555')
        pizza = Meal.objects.get(name='Pizza')
        burger = Meal.objects.get(name='Burger')
        pasta = Meal.objects.get(name='Pasta')
        order1 = Order.objects.create(
            user=regular_user,
            contact_phone=regular_user.phone_number,
            total_price=pizza.price + burger.price + pasta.price,
            status='preparing'
        )
        OrderItem.objects.create(order=order1, meal=pizza,meal_name=pizza.name, quantity=1, unit_price=pizza.price)
        OrderItem.objects.create(order=order1, meal=burger, quantity=1, meal_name=burger.name, unit_price=burger.price)
        OrderItem.objects.create(order=order1, meal=pasta, meal_name=pasta.name, quantity=1, unit_price=pasta.price)

        order2 = Order.objects.create(
            user=admin_user,
            contact_phone=admin_user.phone_number,
            total_price=burger.price * 2,
            status='preparing'
        )

        # عنصر واحد فقط
        OrderItem.objects.create(order=order2, meal=burger,meal_name=burger.name, quantity=2, unit_price=burger.price)

        self.stdout.write(self.style.SUCCESS('✔ Seeded 2*Orders , 3 OrderItems.'))
