from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import *
import random
# Create your views here.

def donate(request):
    typeArray = ['.gif', '.png']
    randomType = random.choice(typeArray)
    if randomType == '.gif':
        randInt = random.randint(1, 2)  # both inclusive
    elif randomType == '.png':
        randInt = random.randint(1, 3)  # both inclusive
    donate_thanks_image_link = '/static/donate/images/donate_thanks'+str(randInt)+randomType
    context = {
        'donate_thanks_image_link' : donate_thanks_image_link
    }
    return render(request, 'donate/donate.html', context)
