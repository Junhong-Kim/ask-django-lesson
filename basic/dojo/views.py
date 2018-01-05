from django.http import HttpResponse
from django.shortcuts import render


def mysum(request, numbers):
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse("Hello, {} ({})".format(name, age))
