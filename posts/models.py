from turtle import title
from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=200)
