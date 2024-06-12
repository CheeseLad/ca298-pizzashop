import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizzashop.settings')
django.setup()

from pizza.models import Size, Crust, Sauce, Cheese, Toppings

sizes_list = [
    'Small',
    'Medium',
    'Large',
    'Extra Large',
    'Party Size',
]

crusts_list = [
    'Thin Crust',
    'Regular Crust',
    'Thick Crust',
    'Stuffed Crust',
    'Gluten Free Crust',
    'Vegan Crust',
]

sauces_list = [
    'Tomato Sauce',
    'Barbecue Sauce',
    'Pesto Sauce',
    'No Sauce',
]

cheeses_list = [
    'Mozzarella',
    'Cheddar',
    'Parmesan',
    'Feta',
    'Gouda',
    'Swiss',
    'Vegan Cheese',
    'Low Fat Cheese',
    'No Cheese',
]

toppings_list = [
    "Pepperoni",
    "Chicken",
    'Ham',
    'Pineapple',
    'Peppers',
    'Mushrooms',
    "Onions",
    "Olives",
    "Sausage",
    "Bacon",
    "Jalapenos",
    "Egg",
    "Spinach",
    "Tomatoes",
    "Artichokes",
    "Anchovies",
    "Basil",
    "Garlic",
    "Pesto",
    "BBQ Chicken",
    "Buffalo Chicken",
    "Meatballs",
    "Shrimp",
]

for size in sizes_list:
    existing_size = Size.objects.filter(size=size).first()
    if not existing_size:
        new_size = Size(size=size)
        new_size.save()
        print(f"Size {size} added successfully.")
    else:
        print(f"Size {size} already exists.")

for crust in crusts_list:
    existing_crust = Crust.objects.filter(crust=crust).first()
    if not existing_crust:
        new_crust = Crust(crust=crust)
        new_crust.save()
        print(f"Crust {crust} added successfully.")
    else:
        print(f"Crust {crust} already exists.")

for sauce in sauces_list:
    existing_sauce = Sauce.objects.filter(sauce=sauce).first()
    if not existing_sauce:
        new_sauce = Sauce(sauce=sauce)
        new_sauce.save()
        print(f"Sauce {sauce} added successfully.")
    else:
        print(f"Sauce {sauce} already exists.")

for cheese in cheeses_list:
    existing_cheese = Cheese.objects.filter(cheese=cheese).first()
    if not existing_cheese:
        new_cheese = Cheese(cheese=cheese)
        new_cheese.save()
        print(f"Cheese {cheese} added successfully.")
    else:
        print(f"Cheese {cheese} already exists.")

for topping in toppings_list:
    existing_topping = Toppings.objects.filter(topping=topping).first()
    if not existing_topping:
        new_topping = Toppings(topping=topping)
        new_topping.save()
        print(f"Topping {topping} added successfully.")
    else:
        print(f"Topping {topping} already exists.")
