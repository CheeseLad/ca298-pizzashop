from django import template
import random

register = template.Library()

@register.filter
def random_number(max_value):
    return random.randint(1, max_value)
