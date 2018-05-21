from django.conf.urls import url
from . import views

app_name = "Donate"

urlpatterns = [
    # /donate/
    url(r'^$', views.donate, name='donate')
]