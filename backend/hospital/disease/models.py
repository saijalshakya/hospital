from django.db import models
from doctor.models import Doctor
from django.utils import timezone
from django.urls import reverse



# Create your models here.
found_choice = (
    ('i', 'Inside KTM Valley'),
    ('o', 'Outside KTM Valley'),
    ('w','Whole Nepal')
)

status_choice = (
    ('1', 'Publish'),
    ('0', 'Unpublished'),
)

class Disease(models.Model):
    name = models.CharField(max_length=500, null=False)
    found = models.CharField(max_length=1, choices=found_choice, null=True)
    summary = models.CharField(max_length=500, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1, choices=status_choice, null=True)
    doctor = models.ManyToManyField(Doctor)

    def publish(self):
        self.status = 1
        self.save()

    def __str__(self):
        return self.name+"-"+self.found

    def get_absolute_url(self):
        return reverse('dashboard:diseases')