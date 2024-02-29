from django.utils.http import urlencode
from serials.models import Genre
from django import template

register = template.Library()


@register.simple_tag()
def tag_genre():
    return Genre.objects.all()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
