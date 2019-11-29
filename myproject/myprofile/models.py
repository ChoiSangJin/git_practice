from django.db import models
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    name=models.CharField(max_length=10)
    introduce=models.TextField(default="")
    age=models.IntegerField(default=0)
    created_data=models.DateTimeField(default=timezone.now)
    published_data=models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_data=timezone.now()
        self.save()



    def __str__(self):
        return self.name

       

