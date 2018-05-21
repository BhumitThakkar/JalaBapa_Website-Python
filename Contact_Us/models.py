from django.db import models

# Create your models here.


class Register(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    @classmethod
    def create(cls, name, email):
        msg = cls(name = name, email = email)
        return msg

    def __str__(self):
        return self.name+"-"+self.email

    '''
    def __init__(self, name, email):
        self.name = name
        self.email = email
    '''

    # Why not to do the above code? : https://docs.djangoproject.com/en/1.7/ref/models/instances/#creating-objects