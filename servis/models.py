from django.db import models

# Create your models here.

class Servis(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    logo=models.URLField(max_length=200)
    
    def __str__(self) -> str:
        return self.name