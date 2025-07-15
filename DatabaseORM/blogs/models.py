from django.db import models
from django.utils import timezone


class Blogger(models.Model):

  '''
  title charfield
  description textfield
  publisher
  rating 
  release_date datefield
  '''

  title = models.CharField(max_length=2048)
  content = models.TextField()
  is_published = models.BooleanField(default=True)
  published_at = models.DateField(default=timezone.now)
  poster = models.ImageField(upload_to="images/", default="images/default.jpg")
