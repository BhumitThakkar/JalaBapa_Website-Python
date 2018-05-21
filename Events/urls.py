from django.conf.urls import url
from . import views

app_name = "Events"

urlpatterns = [
    # /events/
    url(r'^$', views.EventsView.as_view(), name='events'),
    # /events/pk
    url(r'^(?P<pk>[0-9]+)/$', views.EventsDetailView.as_view(), name='details'),
]