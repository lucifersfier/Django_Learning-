from django.http import HttpResponse
from django.shortcuts import render


def main_view(request):
    return render(request,"main/main.html",{"name":"AutoMax"})
# Create your views here.
