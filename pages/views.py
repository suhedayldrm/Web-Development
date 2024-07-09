from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
#show changes in my app

def home(request):
    return render(request, "pages/home.html", {})
