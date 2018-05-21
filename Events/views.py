from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.

class EventsView(generic.ListView):
    template_name = "events/events.html"
    context_object_name = "all_events"

    def get_context_data(self, **kwargs):
        context = super(EventsView, self).get_context_data(**kwargs)
        context['past_events'] = Events.objects.filter(status="Past")
        context['current_events'] = Events.objects.filter(status="Current")
        context['upcoming_events'] = Events.objects.filter(status="Upcoming")
        return context

    def get_queryset(self):
        all_events = Events.objects.all()
        return all_events


class EventsDetailView(generic.DetailView):
    model = Events
    template_name = "events/details.html"
