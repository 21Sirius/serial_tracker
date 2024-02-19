from django.shortcuts import render

from serials.models import Serial


# Create your views here.
def catalog(request, genre_slug):

    if genre_slug == 'vse-serialy':
        serials = Serial.objects.all()
    else:
        serials = Serial.objects.filter(genre__slug=genre_slug)

    context = {
        'title': 'Список сериалов',
        'serials': serials
    }
    return render(request, 'serials/catalog.html', context)


def serial(request, serial_slug=False,):
    serial = Serial.objects.get(slug=serial_slug)

    context = {
        'serial': serial
    }

    return render(request, 'serials/serial.html', context)

