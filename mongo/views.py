from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from django.core.files.storage import default_storage
from .models import *
from .serializers import *


# Create your views here.

@csrf_exempt
def departmentApi(request: object, id=0) -> JsonResponse:
    """Использование CRUD в БД для отделов """
    if request.method == 'GET':
        departaments = Departments.objects.all()
        departaments_serializer = DepartmentSerializer(departaments, many=True)
        return JsonResponse(departaments_serializer.data, safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse('Create Good', safe=False)
        return JsonResponse('Failed', safe=False)
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentsId=department_data['DepartmentsId'])
        departments_serializers = DepartmentSerializer(department, data=department_data)
        if departments_serializers.is_valid():
            departments_serializers.save()
            return JsonResponse('Update Good', safe=False)
        return JsonResponse('Failed', safe=False)
    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentsId=id)
        department.delete()
        return JsonResponse('Delete Good', safe=False)


@csrf_exempt
def employeesApi(request: object, id=0) -> JsonResponse:
    """Использование CRUD в БД для сотрудников """
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployessSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method == 'POST':

        employees_data = JSONParser().parse(request)
        employees_serializer = EmployessSerializer(data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse('Create Good', safe=False)
        return JsonResponse('Failed', safe=False)
    elif request.method == 'PUT':
        employees_data = JSONParser().parse(request)
        employees = Employees.objects.get(EmployeesId=employees_data['EmployeesId'])
        employees_serializers = EmployessSerializer(employees, data=employees_data)
        if employees_serializers.is_valid():
            employees_serializers.save()
            return JsonResponse('Update Good', safe=False)
        return JsonResponse('Failed', safe=False)
    elif request.method == 'DELETE':
        employees = Employees.objects.get(EmployeesId=id)
        employees.delete()
        return JsonResponse('Delete Good', safe=False)


@csrf_exempt
def saveImgApi(request: str) -> JsonResponse:
    """Сохранение images в папке media"""
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)


def index(request):
    """Домашняя страница """
    return render(request, 'mongo/index.html')
