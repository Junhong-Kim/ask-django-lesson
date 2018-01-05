from django.http import HttpResponse
from django.shortcuts import render


def mysum(request, numbers):
    result = sum(map(int, numbers.split("/")))
    return HttpResponse(result)
