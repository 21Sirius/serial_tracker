from django.core.paginator import Paginator
from django.shortcuts import render

from serials.models import Serial


# Create your views here.
def catalog(request, genre_slug):

    page = request.GET.get('page', 1)

    if genre_slug == 'vse-serialy':
        serials = Serial.objects.all()
    else:
        serials = Serial.objects.filter(genre__slug=genre_slug)

    paginator = Paginator(serials, 6)
    current_page = paginator.page(int(page))

    context = {
        'title': 'Список сериалов',
        'serials': current_page,
        'slug_url': genre_slug,
    }
    return render(request, 'serials/catalog.html', context)


def serial(request, serial_slug=False,):
    serial = Serial.objects.get(slug=serial_slug)

    context = {
        'serial': serial
    }

    return render(request, 'serials/serial.html', context)

