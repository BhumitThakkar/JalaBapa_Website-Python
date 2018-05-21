from django.db import models
from django.core.urlresolvers import reverse
from multiselectfield import MultiSelectField           # download= django-multiselectfield  -> https://www.youtube.com/watch?v=5jWJBpS0tkg
from About_Us.models import Authorized_Members
# Create your models here.


class Activities(models.Model):
    activity_title = models.CharField(max_length=100, null=True)
    instructor = models.CharField(max_length=100, null=True)
    start_date = models.DateField(max_length=100, null=True)
    end_date = models.DateField(max_length=100, null=True)
    WEEK_DAYS_CHOICES = (  # (value in database, value on form to choose)
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    )
    week_days = MultiSelectField(choices=WEEK_DAYS_CHOICES, null=True)
    start_time = models.TimeField(max_length=100, null=True)
    end_time = models.TimeField(max_length=100, null=True)
    venue = models.TextField(max_length=500, null=True)
    contact_persons = models.ManyToManyField(Authorized_Members)
    poster = models.FileField(upload_to="activities/")
    summary = models.TextField(max_length=10000, null=True)
    STATUS_CHOICES = (                      # (value in database, value on form to choose)
        ('Past', 'Past'),
        ('Current', 'Current'),
        ('Upcoming', 'Upcoming'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)            # past / current / upcoming

    def get_absolute_url(self):                  # After we submit form, it will redirect to below page
        return reverse("Activities:details", kwargs={'pk':self.pk})


    def __str__(self):
        return self.activity_title+"-"+self.instructor