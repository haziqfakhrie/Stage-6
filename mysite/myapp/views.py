from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

    
def index(request):
    return HttpResponse("Welcome to Stupendous Sloths")

def home_screen_view(request):
    print(request.headers)
    return render(request, "base.html",{})