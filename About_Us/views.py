from django.shortcuts import render
from .models import *

# Create your views here.

def about_us(request):
    all_authorized_members = Authorized_Members.objects.all()
    all_services = Services.objects.all()
    context = {
        "all_authorized_members" : all_authorized_members,
        "all_services" : all_services,
    }
    return render(request, 'about_us/about_us.html', context)
