from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)
    media = models.ImageField(upload_to='posts/', null=True, blank=True) 