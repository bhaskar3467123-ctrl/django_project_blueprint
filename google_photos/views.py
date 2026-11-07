

# Create your views here.


# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django is working google_photos!")
def photos(request):
    return render(request,'google_photos/photos.html')