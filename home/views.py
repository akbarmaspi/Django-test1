from django.http import HttpResponse


def sayhello(request):
    return HttpResponse('Hello Maspi!')
