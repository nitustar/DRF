
from django.urls import path, include

# from .views import CourseList, CourseDetail
from .views import CourseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('course', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('course/', CourseList.as_view(), name='course_detail'),
#     path('course/<int:pk>/', CourseDetail.as_view(), name='course_detail'),
# ]