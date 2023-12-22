from django.http import HttpResponse


def peculiar(request):
    return HttpResponse("you done successful")