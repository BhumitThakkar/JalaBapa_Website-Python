from django.db import models
from multiselectfield import MultiSelectField           # download= django-multiselectfield  -> https://www.youtube.com/watch?v=5jWJBpS0tkg
from django.core.urlresolvers import reverse
from About_Us.models import Authorized_Members

# Create your models here.


class Events(models.Model):
    event_title = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    guest = models.CharField(max_length=500, null=True, blank=True)
    start_date = models.DateField(max_length=100)
    end_date = models.DateField(max_length=100)
    WEEK_DAYS_CHOICES = (  # (value in database, value on form to choose)
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    )
    week_days = MultiSelectField(choices=WEEK_DAYS_CHOICES, null=True, blank=True)
    start_time = models.TimeField(max_length=100)
    end_time = models.TimeField(max_length=100, null=True, blank=True)
    venue = models.TextField(max_length=500)
    contact_persons = models.ManyToManyField(Authorized_Members)
    poster = models.FileField(upload_to="events/")
    summary = models.TextField(max_length=10000)
    STATUS_CHOICES = (
        ('Past', 'Past'),                   # (value, display)
        ('Current', 'Current'),
        ('Upcoming', 'Upcoming'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)            # past / current / upcoming

    def get_absolute_url(self):                  # After we submit form, it will redirect to below page
        return reverse("Events:details", kwargs={'pk':self.pk})

    def __str__(self):
        return self.event_title+"-"+str(self.start_date)
