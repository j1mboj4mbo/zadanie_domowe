"""Definiuje wzorce adresów URL dla library"""

from django.urls import path
from . import views

app_name = "library"
urlpatterns = [
    #strona główna
    path('', views.index, name='index'),
    #aktualny czas
    path('time', views.timing, name='time'),
    #przeglądarka
    path('browser', views.browser, name='browser')
]