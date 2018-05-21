from django.conf.urls import url
from . import views

app_name = "Activities"

urlpatterns = [
    # /activities/
    url(r'^$', views.ActivitiesView.as_view(), name='activities'),
    # /activities/pk
    url(r'^(?P<pk>[0-9]+)/$', views.ActivitiesDetailView.as_view(), name='details'),
    # /activities/add
    url(r'^add/$', views.ActivityCreate.as_view(), name='activity-add')
]