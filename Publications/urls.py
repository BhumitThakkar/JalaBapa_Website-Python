from django.conf.urls import url
from . import views

app_name = "Publications"

urlpatterns = [
    # /publications/
    url(r'^$', views.PublicationsView.as_view(), name='publications'),
    # /publications/Xyz_2017.pdf/
    url(r'(?P<publication>^[A-Za-z_0-9]\.pdf$)', views.PublicationsDetailView.as_view(), name='details')
    # url(r'(?P<pk>^[A-Z][a-z]+\_[0-9]{4}\.pdf$)', views.PublicationsDetailView.as_view(), name='details')
]