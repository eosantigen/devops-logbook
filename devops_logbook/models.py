from django.db import models


class Task(models.Model):

    user = models.CharField(max_length=33)
    time = models.DateTimeField(auto_now_add=True)
    task = models.CharField(max_length=500)
    tags = models.CharField(max_length=100, default="-", null=True)
    
class Tag(models.Model):

    def __str__(self):
        return self.tag

    tag = models.CharField(max_length=30, default="No Tag", primary_key=True)

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"