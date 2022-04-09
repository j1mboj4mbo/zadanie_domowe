from django.shortcuts import render
import datetime
from .models import Book, Author

def index(request):
    """Strona główna"""
    text = ["sprawdzenie aktualnej pogody", "ładniejszy design strony"]
    books = Book.objects.all()
    context = {"text": text, "books": books}
    return render(request, 'library/index.html', context)

def timing(request):
    """Wyświetlanie czasu"""
    current_datetime = datetime.datetime.now()
    context = {"current_datetime": current_datetime}
    return render(request, 'library/time.html', context)

def browser(request):
    browser = request.headers['USER_AGENT'].split()[-1]
    context = {'browser': browser}
    return render(request, 'library/browser.html', context)

def book(request, book_id):
    book = Book.objects.get(id=book_id)
    description = book.description
    author = book.author
    context = {"book": book, "description": description, 'author': author}
    return render(request, 'library/book.html', context)

def author(request, author_id):
    author = Author.objects.get(id=author_id)
    books = author.book_set.all()
    context = {'author': author, "books": books}
    return render(request, 'library/author.html', context)

