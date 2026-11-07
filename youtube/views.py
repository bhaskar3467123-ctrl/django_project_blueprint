from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django is working!")
def youtube(request):
    return render(request,'youtube/youtube.html')