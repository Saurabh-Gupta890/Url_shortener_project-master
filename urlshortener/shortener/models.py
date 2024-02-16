from django.db import models

# Create your models here.
class ShortenedURL(models.Model):
    long_url = models.URLField(unique=True)
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)