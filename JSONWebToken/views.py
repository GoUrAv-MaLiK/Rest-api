from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer
from .models import Student 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
# install simple jwt bt'pip install djangorestframework-simplejwt'
# then create your simple jwt token by using some classes in urls.py
class student_info(ModelViewSet):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]