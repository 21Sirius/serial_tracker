from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        'title': 'STracker',
        'content': 'Трекер сериалов - STracker',
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'STracker - о нас',
        'content': 'О нас',
        'text_on_page': 'STracker-приложение для поиска и отслеживания истории просмотров сериалов',
    }

    return render(request, 'main/about.html', context)
