from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import singer,song
from .serializers import SingerSerializer,SongSerializer

# Create your views here.
class SongView(ModelViewSet):
    serializer_class=SongSerializer
    queryset=song.objects.all()
    
class SingerView(ModelViewSet):
    serializer_class=SingerSerializer
    queryset=singer.objects.all()
