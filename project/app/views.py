from django.shortcuts import render
from django.http import JsonResponse ,HttpResponse
from .models import Student
from .serializers import StudentSerializer
import json

# Create your views here.


def stu_list(req):
    x =Student.objects.all()
    s =  StudentSerializer(x,many =True)
    # print(s)
    # print(s.data)
    # return JsonResponse(s.data ,safe=False)
    jdata=json.dumps(s.data)
    print(jdata)
    return HttpResponse(jdata,content_type ='application/json')


def stu_detail(req ,pk):
    x =Student.objects.all(id = pk)
    s =  StudentSerializer(x)
    # print(s)
    # print(s.data)
    return JsonResponse(s.data ,safe=False)