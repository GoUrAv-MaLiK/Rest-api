from rest_framework import serializers,fields
from .models import song,singer

class SongSerializer(serializers.ModelSerializer):
    class Meta():
        model=song
        fields=['id','title','singer','duration']
        

class SingerSerializer(serializers.ModelSerializer):
    song=serializers.StringRelatedField(many=True,read_only=True)
    class Meta():
        model=singer
        fields=['id','name','gender','song']# thi related name 'song' will give name of songsung by singer
