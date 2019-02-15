from django.db import models
from django.utils import timezone
from django.urls import reverse
from django import forms


class Role(models.Model):
    title = models.CharField(max_length=250, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=0)
    soft = models.BooleanField(default=1)

    def publish(self):
        self.status = 1
        self.save()

    def delete(self):
        self.soft = 0
        self.save()

    def get_absolute_url(self):
        return reverse('dashboard:index', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Players(models.Model):
    fn = models.CharField(max_length=100, null=False, verbose_name="First Name")
    ln = models.CharField(max_length=100, null=False, verbose_name="Last Name")
    phone = models.CharField(max_length=500, null=False, verbose_name="Phone number")
    role = models.ManyToManyField(Role, verbose_name="Role")
    image = models.FileField(verbose_name="User Image")
    address = models.CharField(max_length=500, null=False, verbose_name="Address")
    username = models.CharField(max_length=250, unique=True, null=False, verbose_name="Username")
    password = models.CharField(max_length=500, null=False, verbose_name="Password")
    email = models.CharField(max_length=250, unique=True, null=False, verbose_name="Email")
    created_at = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=0, verbose_name="Status")
    soft = models.BooleanField(default=1)

    def publish(self):
        self.status = 1
        self.save()

    def delete(self):
        self.soft = 0
        self.save()

    def __str__(self):
        return self.fn+" "+self.ln+" - "+"Username: "+self.username

    def get_absolute_url(self):
        return reverse('dashboard:users')
    