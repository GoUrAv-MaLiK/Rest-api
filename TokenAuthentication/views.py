from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication,TokenAuthentication

# Create your views here.
# To start you have to write rest_framework.authtoken in installed apps.
# After this dont't forget to migrate becoz it creates some tabels.
#You can give token to user through admin site through token tabel added previously and you can generate using manage.py dry_create_token {username}
#To generate token from http request go to urls.py file
#To generate token automatically when user login you should use signal (code is in models.py file)
# ---NOW AFTER GENERATING TOKEN. IT IS TIME TO APPLY ON OUR AUTHENTICATION-- 
#to perform operations now write http {url} {for put patch and delete {your data}}'Authoraization:Token {your Token}'
class student_info(ModelViewSet):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]