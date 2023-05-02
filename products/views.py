import io
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .models import Products
from .serializers import ProductsSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def product_api(request):

    # get method    

    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id is not None:
            try:
                stu = Products.objects.get(id=id)
            except Products.DoesNotExist:
                return HttpResponse(status=404)
            serializer = ProductsSerializer(stu)
            return JsonResponse(serializer.data)
        else:
            stu = Products.objects.all()
            serializer = ProductsSerializer(stu, many=True)
            return JsonResponse(serializer.data, safe=False)

   