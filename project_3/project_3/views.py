from django.shortcuts import HttpResponse

def home(req):
    return HttpResponse("This is Home page")