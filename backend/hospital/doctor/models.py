from django.db import models
from django.utils import timezone
# Create your models here.

status_choice = (
    ('1', 'Publish'),
    ('0', 'Unpublished'),
)

class Type(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    created_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1, choices=status_choice, null=True)
    soft = models.BooleanField(default=1)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    price = models.CharField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=0)
    soft = models.BooleanField(default=1)

    def __str__(self):
        return self.name+"-"+self.price

        
class Doctor(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=250, unique=True)
    username = models.CharField(max_length=250, unique=True, null=False)
    password = models.CharField(max_length=800, null=False)
    image = models.FileField(verbose_name="Doctor Image")
    type = models.ManyToManyField(Type)
    service = models.ManyToManyField(Service)
    age = models.CharField(max_length=200, null=False)
    phone1 = models.CharField(max_length=800, null=False)
    phone2 = models.CharField(max_length=800, null=True)
    address = models.CharField(max_length=1000, null=True)
    statement = models.CharField(max_length=5000, null=False)
    educationStatement = models.CharField(max_length=5000, null=False)
    status = models.BooleanField(default=0)
    soft = models.BooleanField(default=1)
    views = models.CharField(max_length=5000, null=True, blank=True, default=0)

    def __str__(self):
        return self.name+" - "+self.username