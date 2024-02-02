from django import template 
from ..models import Home 

register = template.Library() 

@register.simple_tag
def get_info(): 
    info = Home.objects.first()
    return info 
