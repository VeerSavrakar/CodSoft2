from django import template
from courses.models import Course,UserCourse
import math
register = template.Library()

@register.simple_tag
def calculate_total_price(price,discount):
    if discount is None or discount is 0:
        return price
    total=price
    total=price-(price*discount*0.01)
    return math.floor(total)

@register.filter
def rupee(price):
    return f'₹{price}'


@register.simple_tag
def is_enrolled(request,course):
    # is_enrolled=False
    user=None
    if not request.user.is_authenticated:
        return False
    user=request.user
    try:
        user_course=UserCourse.objects.get(user=user,course=course)
        return True
    except:
        return False
    