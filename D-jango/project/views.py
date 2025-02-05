from django.http import HttpResponse

def Home(request):
    return HttpResponse("hello I am Sheelima")

def About(request):
    return HttpResponse("hello")

def Contact(request):
    return HttpResponse("hello I am")
