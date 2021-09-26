from rest_framework import fields,serializers
from .models import Student
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Student
        fields=['id','url','name','roll_no','city']