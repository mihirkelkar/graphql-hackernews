from django.db import models

# Create your models here.


class Link(models.Model):
    url = models.URLField()
    heading = models.CharField(max_length=1000)
    description = models.TextField(blank=True)
