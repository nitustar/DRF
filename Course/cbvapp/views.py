
from rest_framework import mixins, generics
from .models import Course
from .serializers import CourseSerializer
from rest_framework.viewsets import ModelViewSet

from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

# Create your views here.

class CoursePagination(PageNumberPagination):
    page_size = 2

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = LimitOffsetPagination
    # page_size = 2


"""
class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



class CourseList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    

class CourseDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.distory(request, pk)
    
"""

# class CourseList(APIView):

#     def get(self, request):
#         courses = Course.objects.all()
#         serializer = CourseSerializer(courses, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = CourseSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class CourseDetail(APIView):

#     def get_object(self, pk):
#         try:
#             return Course.objects.get(pk=pk)
#         except Course.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#     def get(self, request, pk):
#         serializer= CourseSerializer(self.get_object(pk))
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         serializer = CourseSerializer(self.get_object(pk), data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         self.get_object(pk).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
