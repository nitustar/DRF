from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response

from .models import Course, Instructor
from .serializers import CourseSerializer, InstructorSerializer
# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer