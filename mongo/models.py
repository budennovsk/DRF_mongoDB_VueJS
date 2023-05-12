from django.db import models

# Create your models here.

class Departments(models.Model):
    DepartmentsId = models.AutoField(primary_key=True)
    DepartmentsName = models.CharField(max_length=100)

class Employees(models.Model):
    EmployeesId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    DataJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=100)
