from django.db import models

# Create your models here.

def user_directory_path(instance):
    filename = instance.month_year.strftime("%B_%Y")
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'Publications/media/pdfs/{0}'.format(filename)


class Publications(models.Model):
    file = models.FileField(upload_to="publications/", null=True)            # is uploaded to MEDIA_ROOT/pdfs/ - > in settings.py
    month_year = models.DateField()

    def __str__(self):
        return self.month_year.strftime("%B_%Y")