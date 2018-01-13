from django.http import HttpResponse
# from django.views import View


# class GreetingView(View):
#     message = 'Good Day'
#
#     def get(self, *args, **kwargs):
#         return HttpResponse(self.message)
#
#
# greeting = GreetingView.as_view()
#
#
# class MorningGreetingView(GreetingView):
#     message = 'Morning to ya'
#
#
# morning_greeting = MorningGreetingView.as_view()
# evening_greeting = MorningGreetingView.as_view(message='Evening to ya')


# def greeting(request, message='Good Day'):
#     return HttpResponse(message)
#
#
# def morning_greeting(request):
#     return greeting(request, 'Morning to ya')
#
#
# def evening_greeting(request):
#     return greeting(request, 'Evening to ya')


def greeting_view(message):
    def view_fn(request):
        return HttpResponse(message)
    return view_fn


greeting = greeting_view('Good Day')
morning_greeting = greeting_view('Morning to ya')
evening_greeting = greeting_view('Evening to ya')
