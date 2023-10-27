from django.http import HttpResponse
from django.shortcuts import render


def main_view(request):
    return HttpResponse("<h1>Welcome to AutoMax!</h1>")
# Create your views here.
