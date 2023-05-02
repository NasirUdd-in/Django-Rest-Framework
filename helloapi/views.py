import io
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.



@csrf_exempt
def student_api(request):
    # if request.method == 'GET':
    #     id = request.GET.get('id', None)
    #     if id is not None:
    #         try:
    #             stu = Student.objects.get(id=id)
    #         except Student.DoesNotExist:
    #             return HttpResponse(status=404)
    #         serializer = StudentSerializer(stu)
    #         return JsonResponse(serializer.data)
    #     else:
    #         stu = Student.objects.all()
    #         serializer = StudentSerializer(stu, many=True)
    #         return JsonResponse(serializer.data, safe=False)


    # get method    
    if request.method == 'GET':
       json_data = request.body
       stream = io.BytesIO(json_data)
       pythondata = JSONParser().parse(stream)
       id = pythondata.get('id', None)

       if id is not None:
           stu = Student.objects.get(id=id)
           serializer = StudentSerializer(stu)
           json_data = JSONRenderer().render(serializer.data)
           return HttpResponse(json_data, content_type='application/json')
       
       stu = Student.object.all()
       serializer = StudentSerializer(stu, many =True)
       json_data = JSONRenderer().render(serializer.data)
       return HttpResponse(json_data, content_type='application/json')


    # post method
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data= pythondata)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': "Data Created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')


    # put method
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data = pythondata, partial = True)

        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated !!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')
    

    # delete method
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data Deleted !!'}

        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type = 'application/json')