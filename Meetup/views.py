from django.shortcuts import render

# Create your views here.
def meetup(request):
    context = {
    }
    return render(request, 'meetup/details.html', context)
