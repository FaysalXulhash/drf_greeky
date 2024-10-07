from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


def index(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')

def details(request, pk):
    students = Student.objects.get(pk = pk)
    serializer = StudentSerializer(students)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')