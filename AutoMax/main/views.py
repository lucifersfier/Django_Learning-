from django.shortcuts import render
from django.http import HttpResponse

def landing_view(request):
    return HttpResponse("<h1>Welcome to AutoMax!</h1>")
# Create your views here.
