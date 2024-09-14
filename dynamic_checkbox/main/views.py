from django.shortcuts import render
from django.http import HttpResponse
from .models import checkbox

def home(response):
    return render(response, "main/home.html",{})