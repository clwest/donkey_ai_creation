from django.db import models
from django.conf import settings
from django.utils.text import slugify 
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/%y/%m/%d', null=True, blank=True)
    caption = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)
    disliked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='disliked_posts', blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} by {self.user}"
    
    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)