from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Course
from .serializers import CourseSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def courseListView(request):
    if request.method == 'GET':
        course = Course.objects.all()
        serializer = CourseSerializer(course, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = CourseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)