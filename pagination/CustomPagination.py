from rest_framework.pagination import PageNumberPagination ,LimitOffsetPagination,CursorPagination


class MyPagination(PageNumberPagination):
    page_size=5
    page_query_param='p'
    page_size_query_param='records' #this will override default page size acc to requirments
    # http://127.0.0.1:8000/pagination/?p=2&records=2 if you want this to work you have right query param as shown
    max_page_size=7
    # now if you wrie more than 7 records it will only show 7.

class MyLimitOffset(LimitOffsetPagination):
    # http://127.0.0.1:8000/pagination/?limit=3&offset=8 this way write the query and you can change query param too
    default_limit=5 #5 records default
    limit_query_param='mylimit' #you have to use mylist instead of list
    offset_query_param='myoffset' #you have to use myofffset instead of offset
    max_limit=6 # max 6 records

class MuyCursor(CursorPagination):
    page_size=3 
    ordering='name' #this will order records acc to name
    cursor_query_param='cu' # this will change query param