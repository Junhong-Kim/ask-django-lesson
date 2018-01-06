import os

from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


def mysum(request, numbers):
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse("Hello, {} ({})".format(name, age))


# HttpResponse
def post_list1(request):
    name = 'Kim'
    return HttpResponse('''
        <h1>Ask Django</h1>
        <p>{name}</p>
        <p>Life is too short, You need Python<p>
    '''.format(name=name))


# Template
def post_list2(request):
    name = 'Kim'
    return render(request, 'dojo/post_list.html', {'name': name})


# JsonResponse
def post_list3(request):
    return JsonResponse({
        'message': 'Hello, Python & Django',
        'items': ['Python', 'Django'],
    }, json_dumps_params={'ensure_ascii': False})


# FileDownload
def excel_download(request):
    # os.path.join(settings.BASE_DIR, 'work.xlsx')
    filepath = '/Users/INMA/Downloads/work.xlsx'
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
