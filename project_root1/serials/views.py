from django.shortcuts import render

from serials.models import Serial


# Create your views here.
def catalog(request):
    serials = Serial.objects.all()
    context = {
        'title': 'Список сериалов',
        'serials': serials
    }
    return render(request, 'serials/catalog.html', context)


def serial(request):
    return render(request, 'serials/serial.html')
