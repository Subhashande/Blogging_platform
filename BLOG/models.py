from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    author_name = models.CharField(max_length=100)
    def __str__(self):
        return self.title