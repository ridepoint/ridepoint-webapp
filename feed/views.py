from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def feed(request):
    return render(request, 'feed/feed.html')