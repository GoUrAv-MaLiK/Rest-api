
from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class student_info(ListAPIView):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
    """ filterating data according to a column named pass_by in our table so data appear in concern for a particular user """
    # queryset=Student.objects.filter(pass_by='user')
    #we can make it happen by using django filters and API

    # NOW I WANT LOGGED IN USER DATA IN THIS CASE WE HAVE TO USE GET QUERY SET METHOD
    """ def get_queryset(self):
            print("hello")
            user= self.request.user
            return Student.objects.filter(pass_by=user) """

    # " NOW WE WILL DJANGO-FILTERS FIRST INSTALL USING pip install django-filter AND THEN REGISTER TO SETTINGS.PY FILE"
    # IMPLICITLY FOR ALL VIEWS 
    #GO TO SETTINGS.PY
    # now
    """ filterset_fields=['city'] """
    # NOW FOR FILTER YOU HAVE SEND REQUEST <URL>?FIELD="YOUR VALUE"

    # FOR IMPLICITLY FOR EACH VIEW
    # from django_filters.rest_framework import DjangoFilterBackend
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['city', 'name']


    