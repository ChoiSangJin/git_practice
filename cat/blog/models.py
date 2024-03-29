from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    create_data=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
