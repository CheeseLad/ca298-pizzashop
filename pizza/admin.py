from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Pizza)
admin.site.register(Size)
admin.site.register(Crust)
admin.site.register(Sauce)
admin.site.register(Cheese)
admin.site.register(Toppings)
admin.site.register(PaymentInfo)
admin.site.register(PizzaOrder)