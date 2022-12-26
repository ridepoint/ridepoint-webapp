from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def riders(request):
    return HttpResponse("This is riders")