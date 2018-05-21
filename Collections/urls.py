from django.conf.urls import url
from . import views

app_name = "Collections"

urlpatterns = [
    # /collections/
    url(r'^$', views.CollectionsView, name='collections'),
    url(r'^image_collections/$', views.ImageCollectionsView.as_view(), name='image_collections'),
    url(r'^music_collections/$', views.MusicCollectionsView.as_view(), name='music_collections'),
    url(r'^video_collections/$', views.VideoCollectionsView.as_view(), name='video_collections')
]