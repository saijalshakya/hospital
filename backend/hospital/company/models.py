from django.db import models
from django.utils import timezone
from django.urls import reverse


class Company(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    phone1 = models.CharField(max_length=500, null=True, blank=True)
    phone2 = models.CharField(max_length=500, null=True, blank=True)
    email = models.CharField(max_length=1000, null=True, blank=True)
    facebook = models.CharField(max_length=500, null=True, blank=True)
    instagram = models.CharField(max_length=500, null=True, blank=True)
    twitter = models.CharField(max_length=500, null=True, blank=True)
    youtube = models.CharField(max_length=500, null=True, blank=True)
    fax = models.CharField(max_length=1000, null=True, blank=True)
    pobox = models.CharField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dashboard:company-index')