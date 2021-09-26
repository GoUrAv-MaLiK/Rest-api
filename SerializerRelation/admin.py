from django.contrib import admin
from .models import singer,song
# Register your models here.
@admin.register(singer)
class singerAdmin(admin.ModelAdmin):
    list_display=['id','name','gender']
    
@admin.register(song)
class songAdmin(admin.ModelAdmin):
    list_display=['id','title','singer','duration']
