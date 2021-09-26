from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .CustomPagination import MyPagination,MyLimitOffset,MuyCursor
# Create your views here.
class student_info(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    """ PAGINATION IS CONCEPT TRANSMITTING DATA IN PIECES INSTEAD OF RENDERING WHOLE DATA AT ONCE YOU CAN EXPLICITLY SET UP PAGES AND NO. OF ENTERIES YOU WANT TP RENDER ON THAT PARTICULAR PAGE """
    # TO SET UP PAGINATION CLASS IMPLICITLY FOR ALL VIEWS GO T settings.py file

    #  TO SET UP EXPLICITLY FOR EACH VIEW
    """ pagination_class=MyPagination """
    # now you can set page size in settings.py 

    # CUSTOM PAGINATION 
    #  for this you can inherit a class from PageNumberPagination class
    # and set page size acc to your requirements
    # and you can change page_query_param too from page to anything suitable for
    # and you can set page_size_query_param so that you can explicilty set no of records per page.

    """ LimitOffSetPagination """
    # limit=no. of records offset= start record after ''
    # pagination_class=MyLimitOffset

    """ CURSOR PAGINATION """
    # this will only shoe next and previous button only
    pagination_class=MuyCursor

