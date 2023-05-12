from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'

class EmployessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'