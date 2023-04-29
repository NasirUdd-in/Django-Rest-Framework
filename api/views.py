from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt


#for single data

def student_detail(request, pk):
    # stu = Student.objects.get(id=1)
    stu = Student.objects.get(id = pk)
    #print(stu)
    serializer = StudentSerializer(stu)
    #print(serializer)
    #print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)   
    #print(json_data)
    return HttpResponse(json_data, content_type = 'application/json')
    # return JsonResponse(serializer.data)   #uporer 2 line komia dei



#get all student dat

def student_list(request):
    # stu = Student.objects.get(id=1)
    stu = Student.objects.all()
    #print(stu)
    serializer = StudentSerializer(stu, many = True)
    #print(serializer)
    #print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    #print(json_data)
    return HttpResponse(json_data, content_type = 'application/json')

    # return JsonResponse(json_data, safe=False)


#create data

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data      = request.body
        stream         = io.BytesIO(json_data)
        pythondata     = JSONParser().parse(stream)
        serializer     = StudentSerializer(data = pythondata)

        if serializer.is_valid():
           serializer.save()
           res         = {'msg': 'Data Created'}
           json_data   = JSONRenderer().render(res)
           return HttpResponse(json_data, content_type = 'application/json')
        
        json_data      = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')

    