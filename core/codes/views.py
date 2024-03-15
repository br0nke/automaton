from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.http import HttpRequest, HttpResponse

def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'codes/index.html')