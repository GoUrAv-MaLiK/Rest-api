from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class student_info(ModelViewSet):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
""" authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated] """
    # if there are more than one classes and all need authentication then we don't need to rewrite our code we can setup authentication implicitly in settings.py file and if one of the class does not require authentication we can set it up explicitly 
    