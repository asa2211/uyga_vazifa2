from django.http import HttpResponse


def get_name(request):
    return HttpResponse('hello from sarvar1')
def get_name2(request):
    return HttpResponse('hello from sarvar2')
