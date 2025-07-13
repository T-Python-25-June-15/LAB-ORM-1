from django.db import models
from datetime import date

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=2024)
    content = models.TextField(default='none')
    is_published = models.BooleanField(default=True)
    published_at = models.DateField(default=date.today)