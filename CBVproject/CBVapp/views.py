from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from CBVapp.models import Course, CourseSerializer
# Create your views here.

class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

class CourseDetailView(APIView):
    def get_course(self, pk):
        try:
            return Course.objects.get(pk = pk)
        except Course.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        course = self.get_course(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def delete(self, request, pk):
        self.get_course(pk).delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        serializer = CourseSerializer(self.get_course(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)  
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)