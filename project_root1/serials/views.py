from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404

from serials.models import Serial

from serials.utils import q_search


# Create your views here.
def catalog(request, genre_slug=None):
    page = request.GET.get('page', 1)
    top_on_top = request.GET.get('top_on_top', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if genre_slug == 'vse-serialy':
        serials = Serial.objects.all()

    elif query:
        serials = q_search(query)

    else:
        serials = Serial.objects.filter(genre__slug=genre_slug)

    if top_on_top:
        serials = serials.filter(rating__gt=8.5)

    if order_by and order_by != 'default':
        serials = serials.order_by(order_by)

    paginator = Paginator(serials, 6)
    current_page = paginator.page(int(page))

    context = {
        'title': 'Список сериалов',
        'serials': current_page,
        'slug_url': genre_slug,
    }
    return render(request, 'serials/catalog.html', context)


def serial(request, serial_slug=False, ):
    serial = Serial.objects.get(slug=serial_slug)

    context = {
        'serial': serial
    }

    return render(request, 'serials/serial.html', context)
