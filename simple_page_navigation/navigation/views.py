from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def about(request):
    return render(request, "navigation/about.html")

def contact(request):
    return render(request, "navigation/contact.html")