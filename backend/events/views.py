from django.shortcuts import render

from shortcuts import RequestType, HttpResponse


def index(request: RequestType) -> HttpResponse:
    return render(request, 'index.html')
