from django.db import models
from rest_framework import serializers

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length = 100)
    price = models.IntegerField()
    discount = models.IntegerField()
    duration = models.FloatField()
    author_name = models.CharField(max_length = 100)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"