from rest_framework import serializers




class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    email = serializers.EmailField()
    roll_no = serializers.CharField(max_length=20)
    grade = serializers.CharField(max_length=10)


# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student   # kis model ka serializer hai
#         fields = '__all__'   