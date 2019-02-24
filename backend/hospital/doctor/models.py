from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
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
    counter = models.CharField(max_length=1000, default=0, null=True, blank=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    price = models.CharField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=0)
    soft = models.BooleanField(default=1)

    def __str__(self):
        return self.name

        
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    image = models.FileField(verbose_name="Doctor Image")
    type = models.ManyToManyField(Type)
    service = models.ManyToManyField(Service)
    age = models.CharField(max_length=200, null=False)
    phone1 = models.CharField(max_length=800, null=False)
    phone2 = models.CharField(max_length=800, null=True)
    address = models.CharField(max_length=1000, null=True)
    statement = models.CharField(max_length=5000, null=False)
    educationStatement = models.CharField(max_length=5000, null=False)
    status = models.CharField(max_length=1, choices=status_choice, null=True)
    soft = models.BooleanField(default=1)
    views = models.CharField(max_length=5000, null=True, blank=True, default=0)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('dashboard:profile-save')

confirm_choice = (
    ('1', 'Confirmed'),
    ('0', 'Unconfirmed'),
)

checked_choice = (
    ('1', 'Checked'),
    ('0', 'Unchecked'),
)

class Booking(models.Model):
    service = models.CharField(max_length = 500, null = False, blank = False)
    doctor = models.ManyToManyField(Doctor)
    fn = models.CharField(max_length = 100, null = False, blank = False)
    ln = models.CharField(max_length = 100, null = False, blank = False)
    email = models.CharField(max_length = 500, null = True, blank = True)
    phone = models.CharField(max_length = 800, null = False, blank = False)
    location = models.CharField(max_length=300, null = False, blank = False)
    street1 = models.CharField(max_length=200, null = False, blank = False)
    street2 = models.CharField(max_length=200, null = True, blank = True)
    city = models.CharField(max_length=200, null = False, blank = False)
    state = models.CharField(max_length=100, null = True, blank = True)
    postal = models.CharField(max_length=100, null = True, blank = True)
    confirm = models.CharField(max_length=1, choices=confirm_choice, default = "0",null=False, blank = False)
    checked = models.CharField(max_length=1, choices=checked_choice, default = "0",null=False, blank = False)
    treatment = models.CharField(max_length=1000, null = True, blank = True)
    next  = models.CharField(max_length=1000, null = True, blank = True)
    note = models.CharField(max_length=1000, null = True, blank = True)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.fn+" "+self.ln

class Review(models.Model):
    rate = models.CharField(max_length=100,null=False, blank=False)
    doctor = models.ManyToManyField(Doctor)
    title = models.CharField(max_length=500, null=False, blank=False)
    rev   = models.CharField(max_length=1000, null=False, blank=False)
    status = models.CharField(max_length=1, choices=status_choice, null=True, default=0)

    def __str__(self):
        return self.title