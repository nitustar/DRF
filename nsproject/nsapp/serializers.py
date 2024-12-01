from rest_framework import serializers

from .models import Course, Instructor

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class InstructorSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)           # This is a nested serializer

    class Meta:
        model = Instructor
        fields = "__all__"