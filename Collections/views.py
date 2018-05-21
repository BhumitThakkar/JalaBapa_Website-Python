from django.views import generic
from django.shortcuts import render
from .models import *

# Create your views here.


def CollectionsView(request):
    return render(request, 'collections/collections.html')


class ImageCollectionsView(generic.ListView):
    template_name = 'collections/image_collection.html'
    context_object_name = "image_collection"

    def get_queryset(self):
        return ImageCollection.objects.all()


class MusicCollectionsView(generic.ListView):
    template_name = 'collections/music_collection.html'
    context_object_name = "music_collection"

    def get_queryset(self):
        return MusicCollection.objects.all()


class VideoCollectionsView(generic.ListView):
    template_name = 'collections/video_collection.html'
    context_object_name = "video_collection"

    def get_queryset(self):
        return VideoCollection.objects.all()
