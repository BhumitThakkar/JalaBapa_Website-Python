from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.

class ActivitiesView(generic.ListView):
    template_name = "activities/activities.html"
    context_object_name = "all_activities"

    def get_queryset(self):
        return Activities.objects.all()


class ActivitiesDetailView(generic.DetailView):
    model = Activities
    template_name = "activities/details.html"


class ActivityCreate(CreateView):
    model = Activities
    fields = ['activity_title', 'instructor', 'start_date', 'end_date', 'week_days', 'timings', 'venue', 'contact_persons', 'poster', 'summary', 'status']
