from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    ratings = models.IntegerField()

    def __str__(self):
        return self.name