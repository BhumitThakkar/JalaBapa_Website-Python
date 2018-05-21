from django.db import models
# Create your models here.

class Authorized_Members(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    BOARD_CHOICES = (
        ('PRIEST', 'PRIEST'),
        ('TRUST', 'TRUST'),
        ('EXECUTIVE', 'EXECUTIVE'),
    )
    board = models.CharField(max_length=10, choices=BOARD_CHOICES)

    def __str__(self):
        return self.first_name+" "+self.last_name


class Services(models.Model):
    service_title = models.CharField(max_length=100)
    associated_members = models.ManyToManyField(Authorized_Members)

    def __str__(self):
        return self.service_title

# a = Authorized_Members.objects.get(id=2)
# print(a.services_set.all)                  when calling through object remove brackets after all
# print(Services.objects.get(id=2).associated_members.all)