from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser ,IsAuthenticated, IsAuthenticatedOrReadOnly,DjangoModelPermissions
from .custom_permisssions import MyPermissions

# Create your views here.
class student_info(ModelViewSet):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
    authentication_classes=[SessionAuthentication]
    #session authentication provides login logout button if we mention rest_framework.urls explicitly in urls.py
    permission_classes=[IsAuthenticated]
    # 'any user can acces and write data if logged in'
    """ permission_classes=[AllowAny] """
    # 'annonmous can read and write '
    """ permission_classes=[IsAdminUser] """
    #'admin and staff true user can read and write'
    """ permission_classes=[IsAuthenticatedOrReadOnly] """
    # 'if authenticated=all operations if not thne read only permission'
    # permission_classes=[MyPermissions]
    # 'you can explicitly assign pemission to user after logging in admin page but if user and if user is staff then it have all permissions'