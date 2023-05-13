"""
URL configuration for DRF_mongoDB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import re_path, path
from mongo import views

urlpatterns = [

    # Использование API методами CRUD для отделов

    re_path(r'^departament$', views.departmentApi, name='departmentApi'),
    re_path(r'^departament/([0-9]+)$', views.departmentApi, name='departmentApi'),

    # Использование API методами CRUD для сотрудников

    re_path(r'^employees$', views.employeesApi, name='employeesApi'),
    re_path(r'^employees/([0-9]+)$', views.employeesApi, name='employeesApi'),

    # Использование маршрута для добавления картинок

    re_path(r'^employees/file', views.saveImgApi, name='saveImgApi'),

    path("", views.index, name='index'),

]
