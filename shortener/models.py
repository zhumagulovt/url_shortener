from django.db import models
from django.contrib.auth.models import User

class ShortUrl(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    short_url = models.CharField(max_length=10)
    long_url = models.TextField()

    def __str__(self):
        return self.short_url