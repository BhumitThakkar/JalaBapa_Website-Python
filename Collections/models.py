from django.db import models
from django.core.urlresolvers import reverse
import os
# Create your models here.


class ImageCollection(models.Model):
    file = models.FileField(upload_to="Collections/image", max_length=200)
    file_name = models.CharField(max_length=100)

    def get_absolute_url(self):                  # After we submit form, it will redirect to below page
        # return reverse("Collections:collections", kwargs={'pk': self.pk})         # kwargs not needed here
        return reverse("Collections:collections")

    def __str__(self):
        return self.file_name


class MusicCollection(models.Model):
    file = models.FileField(upload_to='Collections/music', max_length=200)
    file_name = models.CharField(max_length=100)

    def __str__(self):
        return self.file_name


class VideoCollection(models.Model):
    file = models.FileField(upload_to='Collections/video', max_length=200)
    file_name = models.CharField(max_length=100)

    def __str__(self):
        return self.file_name
