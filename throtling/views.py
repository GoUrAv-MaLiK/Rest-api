from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer
from .models import Student 
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
#throttling explicitly for diff views
from .throttling import CustomRateThrottle

class student_info(ModelViewSet):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    #NOW WE'LL USE CONCEPT OF THROTTLE THROUGH WHICH WE CAN RESTRICT THE NUMBER OF REQUEST OF A PARTICULAR USER ON OUR API
    throttle_classes=[AnonRateThrottle,CustomRateThrottle]
    #now go to settings to set rate for user
    #to set explicitly for every view create a new file throttling.py and write your code
