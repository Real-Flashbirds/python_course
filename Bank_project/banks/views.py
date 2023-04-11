from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the banks index.")


def personal_test(request):
    return HttpResponse("This is your personnal test")