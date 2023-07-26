from django.http import HttpResponse


def get_name(request):
    return HttpResponse('hi django1')


def get_name2(request):
    return HttpResponse('hi django2')
