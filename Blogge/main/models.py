
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=1024)
    content = models.TextField(max_length=256)
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

