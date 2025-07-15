from django.db import models
from django.utils import timezone

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=2048)
    content= models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateField(default=timezone.now)
    image= models.ImageField(upload_to="images/", default="images/default.jpg")
