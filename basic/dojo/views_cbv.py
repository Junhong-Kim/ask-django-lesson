import os

from django.http import JsonResponse, HttpResponse
from django.views.generic import View, TemplateView


# HttpResponse
class PostListView1(View):
    def get(self, request):
        name = 'Kim'
        html = self.get_template_string().format(name=name)

        return HttpResponse(html)

    def get_template_string(self):
        return '''
            <h1>Ask Django</h1>
            <p>{name}</p>
            <p>Life is too short, You need Python<p>
        '''


post_list1 = PostListView1.as_view()


# Template
class PostListView2(TemplateView):
    template_name = 'dojo/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['name'] = 'Kim'
        return context


post_list2 = PostListView2.as_view()


# JsonResponse
class PostListView3(View):
    def get(self, request):
        return JsonResponse(self.get_data(), json_dumps_params={'ensure_ascii': False})

    def get_data(self):
        return {
            'message': 'Hello, Python & Django',
            'items': ['Python', 'Django'],
        }


post_list3 = PostListView3.as_view()


# FileDownload
class ExcelDownloadView(View):
    filepath = '/Users/INMA/Downloads/work.xlsx'

    def get(self, request):
        # os.path.join(settings.BASE_DIR, 'work.xlsx')
        filename = os.path.basename(self.filepath)

        with open(self.filepath, 'rb') as f:
            response = HttpResponse(f, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
            return response


excel_download = ExcelDownloadView.as_view()
