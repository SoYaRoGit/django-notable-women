from django.http import HttpResponse


def index(request) -> HttpResponse:
    return HttpResponse("Стартовая страничка")


def categories(request) -> HttpResponse:
    return HttpResponse("<h1>Статьи по категориям</h1>")
