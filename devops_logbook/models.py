import datetime
from django.db import models
from django.utils import timezone


class Task(models.Model):

    user = models.CharField(max_length=33)
    time = models.CharField(max_length=333)
    task = models.CharField(max_length=500)
    tags = models.CharField(max_length=100, default="-", null=True)

class Tag(models.Model):

    def __str__(self):
        return self.tag

    tag = models.CharField(max_length=30, default="-", primary_key=True)

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"