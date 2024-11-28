from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics, mixins
from rest_framework.viewsets import ViewSet, ModelViewSet

from CBVapp.models import Course, CourseSerializer
# Create your views here.

# ModelViewSets

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


'''
# ViewSets

class CourseViewSet(ViewSet):
    def list(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
        serializer = CourseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk):
        try:
            course = Course.objects.get(pk = pk)
        except Course.DoesNotExist:
            raise Http404
        serializer = CourseSerializer(course)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        try:
            course = Course.objects.get(pk = pk)
        except Course.DoesNotExist:
            raise Http404
        course.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
'''


# Generic API Views

'''
class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
'''


# Generic API Views with mixins

'''
class CourseListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    

class CourseDetailView(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)

'''

# Class Based Views

'''
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

'''