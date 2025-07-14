from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published= models.BooleanField(default=True)
    published_at = models.DateField(default=datetime.now())
    image = models.ImageField(upload_to="images/",default='images/default.jpg')