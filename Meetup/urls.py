from django.conf.urls import url
from . import views

app_name = "Meetup"

urlpatterns = [
    # /meetup/
    url(r'^$', views.meetup, name='meetup'),
]