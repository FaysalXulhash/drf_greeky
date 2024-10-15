from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


@api_view(['GET', 'POST'])
def student_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def student_details_api(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'updated!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)














# # create, retrive, update, delete 
# @csrf_exempt
# def student_api(request):
#     if request.method == 'GET':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id', None)
#         if id is not None:
#             student = Student.objects.get(id=id)
#             serializer = StudentSerializer(student)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type = 'application/json')

#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type = 'application/json')
    
#     #create new student
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Successfully created!'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
    
#     #update student
#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         student = Student.objects.get(id=id)
#         serializer = StudentSerializer(student, data=pythondata, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': f'Successfully updated student - {id}.'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
#     # delete studet
#     if request.method == 'DELETE':
#         json_data = request.body
#         print(json_data)
#         stream = io.BytesIO(json_data)
#         print(stream)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         student = Student.objects.get(id=id)
#         student.delete()
#         res = {'msg': f'successfully deleted student - {id}!'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type='application/json')

