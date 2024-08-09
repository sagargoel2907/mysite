from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Answer to the Ultimate Question")


def owner(request):
    return HttpResponse("Hello, world. 74398c40 is the polls owner.")
