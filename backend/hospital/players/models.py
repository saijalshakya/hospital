from django.db import models
from django.utils import timezone


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

    def __str__(self):
        return self.title


class Players(models.Model):
    fn = models.CharField(max_length=100, null=False)
    ln = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=500, null=False)
    role = models.OneToOneField(Role, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to="img/user")
    address = models.CharField(max_length=500, null=False)
    username = models.CharField(max_length=250, unique=True, null=False)
    password = models.CharField(max_length=500, null=False)
    email = models.CharField(max_length=250, unique=True, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=0)
    soft = models.BooleanField(default=1)

    def publish(self):
        self.status = 1
        self.save()

    def delete(self):
        self.soft = 0
        self.save()

    def __str__(self):
        return self.fn+" "+self.ln+" - "+"Username: "+self.username