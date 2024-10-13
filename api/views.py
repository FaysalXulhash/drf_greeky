from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
import io
from django.views.decorators.csrf import csrf_exempt


# create, retrive, update, delete 
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'application/json')

        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = 'application/json')
    
    #create new student
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Successfully created!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    #update student
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': f'Successfully updated student - {id}.'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    # delete studet
    if request.method == 'DELETE':
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        print(stream)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        student = Student.objects.get(id=id)
        student.delete()
        res = {'msg': f'successfully deleted student - {id}!'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')




# def index(request):
#     students = Student.objects.all()
#     serializer = StudentSerializer(students, many=True)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type = 'application/json')

# def details(request, pk):
#     students = Student.objects.get(pk = pk)
#     serializer = StudentSerializer(students)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type = 'application/json')

# #creating new student
# @csrf_exempt
# def create_student(request):
#     if request.method == 'POST':
#         json_data = request.body
#         print('json_Data: ', json_data)
#         stream = io.BytesIO(json_data)
#         print('stream: ', stream)
#         pythondata = JSONParser().parse(stream)
#         print('python-data: ', pythondata)
#         serializer = StudentSerializer(data= pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'data inserted successfully'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type= 'appllication/json' )
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type= 'appllication/json' )