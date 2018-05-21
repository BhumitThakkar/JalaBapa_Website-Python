from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import *

# Create your views here.

def home(request):
    return render(request, 'home/home.html')
