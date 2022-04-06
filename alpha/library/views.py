from django.shortcuts import render
import datetime

def index(request):
    """Strona główna"""
    text = ["sprawdzenie aktualnej pogody", "ładniejszy design strony"]
    context = {"text": text}
    return render(request, 'library/index.html', context)

def timing(request):
    """Wyświetlanie czasu"""
    current_datetime = datetime.datetime.now()
    context = {"current_datetime": current_datetime}
    return render(request, 'library/time.html', context)

def browser(request):
    browser = request.META['HTTP_USER_AGENT']
    context = {'browser': browser}
    return render(request, 'library/browser.html', context)





