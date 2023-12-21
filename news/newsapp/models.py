from django.db import models

# Create your models here.

# news/models.py

class News(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    summary = models.TextField()
    published = models.DateTimeField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title

