import os

from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from .forms import PostForm
from .models import Post


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # 방법 1)
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()

            # 방법 2)
            # post = Post(title=form.cleaned_data['title'],
            #             content=form.cleaned_data['content'])
            # post.save()

            # 방법 3)
            # post = Post.objects.create(title=form.cleaned_data['title'],
            #                            content=form.cleaned_data['content'])

            # 방법 4)
            # post = Post.objects.create(**form.cleaned_data)

            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()

            return redirect('/dojo/')
    else:
        form = PostForm()

    return render(request, 'dojo/post_form.html', {
        'form': form,
    })


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
