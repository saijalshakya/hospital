from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

# Create your models here.

status_choice = (
    ('1', 'Publish'),
    ('0', 'Unpublished'),
)

type_choice = (
    ('1', 'News'),
    ('0', 'Events'),
)

class Blogs(models.Model):
    title = models.CharField(max_length=300, null=False, blank = False)
    intro = models.CharField(max_length=200,null=False, blank = False)
    description = models.CharField(max_length = 1000, null=False, blank = False)
    image = models.FileField(verbose_name="Blogs Image")
    status = models.CharField(max_length=1, choices=status_choice, null=False, blank = False)
    types = models.CharField(max_length=1, choices=type_choice, null=False, blank = False)
    created_at = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.status = 1
        self.save()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
            return reverse('dashboard:blogs')