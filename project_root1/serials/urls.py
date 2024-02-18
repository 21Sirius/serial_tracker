from django.urls import path

from serials import views

app_name = 'serials'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('serial/', views.serial, name='serial')

]
