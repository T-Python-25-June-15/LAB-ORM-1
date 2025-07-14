from django.db import models
from django.db.models import Model
# Create your models here.


class Post(Model):
    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    
    def __str__(self):
        return self.title