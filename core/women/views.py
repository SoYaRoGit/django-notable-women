from django.http import HttpResponse


def index(request) -> HttpResponse:
    return HttpResponse("Стартовая страничка")


def categories(request, cat_id) -> HttpResponse:
    return HttpResponse(f"<h1>Статьи по категориям id={cat_id}</h1>")


def archive(request, year: int) -> HttpResponse:
    return HttpResponse(f"<h1>Архив по годам Год: {year}</h1>")
