# from django.shortcuts import render
# from django.http import JsonResponse ,HttpResponse
# from .models import Student
# from .serializers import StudentSerializer
# import json
# from django.views.decorators.csrf import csrf_exempt

# # Create your views here.
# csrf_exempt


# def stu_list(req):
#     if req.method == 'POST':
#         print('post')
#         print(req.body)
#         data = json.loads(req.body)
#         print(data)
#         print(type(data))
#         Student.object.create(name =data['name'] ,age = data['age'] ,email =data['email'])
#         print('data save succeesssssssss')
        
#     else:    
#      x =Student.objects.all()
#      s =  StudentSerializer(x,many =True)
#     # print(s)
#     # print(s.data)
#     # return JsonResponse(s.data ,safe=False)
#      jdata=json.dumps(s.data)
#      print(jdata)
#      return HttpResponse(jdata,content_type ='application/json')


# def stu_detail(req ,pk):
#     x =Student.objects.get(id = pk)
#     s =  StudentSerializer(x)
#     # print(s)
#     # print(s.data)
#     return JsonResponse(s.data ,safe=False)


from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Student
from .serializers import StudentSerializer
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt   # 👈 yaha decorator lagana zaroori hai
def stu_list(req):
    if req.method == 'POST':
        print('post')
        print(req.body)
        
        # body se JSON data nikaalo
        data = json.loads(req.body)
        print(data)
        print(type(data))
        
        # student create karo
        Student.objects.create(
            name=data['name'],
            age=data['age'],
            email=data['email'],
            roll_no=data['roll_no'],   # required field
            grade=data.get('grade')    # optional
        )
        print('data save succeesssssssss')
        
        # success response bhejna zaruri hai
        return JsonResponse({"message": "Student created successfully!"})

    else:
        x = Student.objects.all()
        s = StudentSerializer(x, many=True)
        return JsonResponse(s.data, safe=False)

#  DLT WITH URL ID
# @csrf_exempt   # 👈 detail view pe bhi lagana padega agar POST/PUT karna hai
# def stu_detail(req ,pk):
#      if req.method == "DELETE":
#         id=pk
#         x = Student.objects.get(id=id)
#         x.delete()
#         return JsonResponse({"message": "Student deleted successfully"})

# DLT WITH BODY.REQ

@csrf_exempt   # 👈 detail view pe bhi lagana padega agar POST/PUT karna hai
def stu_detail(req  ):
     if req.method == "DELETE":
          json_data = req.body
          py_data =json.loads(json_data)
          print("Request Body JSON:", py_data)
          id = int(py_data.get('id'))
          print(id)
          x = Student.objects.get(id=id)
          x.delete()
          return JsonResponse({"message": "object deleted successfully"})
     elif req.method == 'PATCH':
          x = Student.objects.get(id=3)
          p_data = json.loads(req.body)
          x.name =p_data['name']
          x.save()
          return JsonResponse({"message": "object partial updated successfully"})
         
     elif req.method == 'PUT':
          x = Student.objects.get(id=3)
          p_data = json.loads(req.body)
          x.name =p_data['name']
          
          x.save()
          return JsonResponse({"message": "object updated successfully"})


