from django.conf.urls import url
from . import views

app_name = "About_Us"

urlpatterns = [
    # /about_us/
    url(r'^$', views.about_us, name='about_us'),
]
