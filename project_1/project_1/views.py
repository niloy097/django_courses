from django.http import HttpResponse

def home(request):
    return HttpResponse("This is homepage")

def contact(reuqest):
    return HttpResponse("This is contact Page")


