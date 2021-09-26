from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer
from .models import Student 
from rest_framework.permissions import IsAuthenticated
from .CustomAuthentication import customauthentication
from rest_framework.authentication import BasicAuthentication,SessionAuthentication

# Create your views here.
# create your own custom authentication file
class student_info(ModelViewSet):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]