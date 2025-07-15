from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    class RatingsChoises(models.IntegerChoices):
        STAR1 = 1, "One Star"
        STAR2 = 2, "Two Stars"
        STAR3 = 3, "Three Stars"
        STAR4 = 4, "Four Stars"
        STAR5 = 5, "Five Stars"

    title = models.CharField(max_length=2048)
    content = models.TextField()
    rtaing = models.SmallIntegerField(choices=RatingsChoises.choices, default= 0) 
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)

    def __str__(self):
        return self.title




