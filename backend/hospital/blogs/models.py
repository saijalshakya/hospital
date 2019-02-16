from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

# Create your models here.

status_choice = (
    ('1', 'Publish'),
    ('0', 'Unpublished'),
)

class Blogs(models.Model):
    title = models.CharField(max_length=300, null=False)
    intro = models.CharField(max_length=200,null=False)
    description = models.CharField(max_length = 1000, null=False)
    image = models.FileField(verbose_name="Blogs Image")
    status = models.CharField(max_length=1, choices=status_choice, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.status = 1
        self.save()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
            return reverse('dashboard:blogs')