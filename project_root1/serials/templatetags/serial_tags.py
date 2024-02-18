from serials.models import Genre
from django import template

register = template.Library()


@register.simple_tag()
def tag_genre():
    return Genre.objects.all()
