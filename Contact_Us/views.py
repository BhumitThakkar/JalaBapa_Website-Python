from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import *
import random

# Create your views here.

def contact_us(request):
    return render(request, 'contact_us/contact_us.html')

def regiser(request):
    if request.POST:
        name = request.POST.get('Name', "Default")
        email = request.POST.get('Email', "Default")

        msg_obj = Register.create(name, email)
        msg_obj.save()
        # request.POST = {}         not required now, now when refresh no form resubmission and no data will be sent again
        return HttpResponseRedirect("/contact_us/thanks/")
    else:
        raise Http404("Page Not Found")

def thanks(request):
    typeArray = ['.gif', '.png']
    randomType = random.choice(typeArray)
    if randomType == '.gif':
        randInt = random.randint(1, 3)  # both inclusive
    elif randomType == '.png':
        randInt = random.randint(1, 2)  # both inclusive
    thanks_image_link = '/static/contact_us/images/thanks'+str(randInt)+randomType
    context = {
        'thanks_image_link' : thanks_image_link
    }
    return render(request, 'contact_us/contact_us.html', context)