from django.shortcuts import render
from django.http import HttpResponse
from .models import checkbox

def index(response):
    return HttpResponse("<h1>test</h1>")