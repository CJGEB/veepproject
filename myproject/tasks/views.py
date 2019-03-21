from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

def detail(request, item_nbr):
    return HttpResponse("You are looking at tasks %s." % item_nbr)
