from .models import Employee

from rest_framework import serializers
from django.contrib.auth.models import User

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=30)
    phone = serializers.CharField(max_length=10)

    def create(self, validated_data):
        print("Create Method for employee is called..")
        return Employee.objects.create(**validated_data)
    
    def update(self, employee, validated_data):
        newEmployee = Employee(**validated_data)
        newEmployee.id = employee.id
        newEmployee.save()
        return newEmployee


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
    is_staff = serializers.BooleanField()

    def create(self, validated_data):
        print("Create Method for user is called..")
        return User.objects.create(**validated_data)

