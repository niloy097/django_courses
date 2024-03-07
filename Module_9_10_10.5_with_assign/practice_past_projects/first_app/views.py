from django.shortcuts import render
from django.shortcuts import HttpResponse
def home(request):
    return HttpResponse("This is firstapp Home Page")

def about(request):
    return HttpResponse("This is first app about page")
