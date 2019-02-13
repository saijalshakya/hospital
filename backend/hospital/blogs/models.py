from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.


class Blogs(models.Model):
    title = models.CharField(max_length=300, null=False)
    intro = models.CharField(max_length=200,null=False)
    description = models.CharField(max_length = 1000, null=False)
    image = models.ImageField(upload_to="blog_image", blank = True)
    status = models.BooleanField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.status = 1
        self.save()

    def __str__(self):
        return self.title