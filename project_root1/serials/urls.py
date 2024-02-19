from django.urls import path

from serials import views

app_name = 'serials'

urlpatterns = [
    path('<slug:genre_slug>', views.catalog, name='index'),
    path('serial/<slug:serial_slug>/', views.serial, name='serial'),

]
