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
    path('browser', views.browser, name='browser'),
    #książka
    path('books/<int:book_id>/', views.book, name='book'),
    #autor
    path('author/<int:author_id>/', views.author, name='author')
]