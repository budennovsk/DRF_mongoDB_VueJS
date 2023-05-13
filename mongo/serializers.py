from rest_framework import serializers

from .models import *


class DepartmentSerializer(serializers.ModelSerializer):
    """Сериализация БД отделов сотрудников"""
    class Meta:
        model = Departments
        fields = '__all__'

class EmployessSerializer(serializers.ModelSerializer):
    """Сериализация БД сотрудников отдела"""
    class Meta:
        model = Employees
        fields = '__all__'