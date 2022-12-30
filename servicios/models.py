from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.URLField(max_length=255)

    def __str__(self) -> str:
        return self.name