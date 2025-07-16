from django.db import models
from django.utils import timezone 

# Create your models here.

class Post(models.Model):#hey django, please turn this class inti a db table and give it db features
    '''
    - title : char field (max 2048)
    - content : text field.
    - is_published : boolean field, default is True.
    - published_at : datetime field, default is now.
    '''
    title = models.CharField(max_length = 2048)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="posts_images/", null=True, blank=True)

    #after creating that run the makemigration and migrate commands 