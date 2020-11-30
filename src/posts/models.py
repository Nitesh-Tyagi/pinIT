from django.db import models
import datetime
from django import forms
import time
# Create your models here.


class Post(models.Model):
    text = models.TextField()
    # created_date = models.DateField(default=_datetime.date.today())
    # created_time = models.TimeField(default=datetime.now())
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
