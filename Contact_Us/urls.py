from django.conf.urls import url
from . import views

app_name = "Contact_Us"

urlpatterns = [
    # /contact_us/
    url(r'^$', views.contact_us, name='contact_us'),
    # /contact_us/sendNote/
    url(r'^sendNote/$', views.regiser, name='regiser'),
    # /contact_us/thanks
    url(r'^thanks/$', views.thanks, name='thanks'),
]