from django.db import models

# Create your models here.


class Doctor(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=250, unique=True)
    username = models.CharField(max_length=250, unique=True, null=False)
    password = models.CharField(max_length=800, null=False)
    image = models.ImageField(upload_to="doctor_image", blank = True)
    age = models.CharField(max_length=200, null=False)
    phone1 = models.CharField(max_length=800, null=False)
    phone2 = models.CharField(max_length=800, null=True)
    address = models.CharField(max_length=1000, null=True)
    statement = models.CharField(max_length=5000, null=False)
    educationStatement = models.CharField(max_length=5000, null=False)
    status = models.BooleanField(default=0)
    soft = models.BooleanField(default=1)

    def __str__(self):
        return self.name+" - "+self.username