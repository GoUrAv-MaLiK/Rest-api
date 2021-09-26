from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class singer(models.Model):
    name=models.CharField( max_length=50)
    gender=models.CharField( max_length=50)

    def __str__(self):
        return self.name
class song(models.Model):
    title=models.CharField( max_length=50)
    singer=models.ForeignKey(singer, on_delete=models.CASCADE, related_name='song')#related name is used for serializer relations if you want to show song sung by the singer on singer's url you'll use it.

    duration=models.IntegerField()
    
    def __str__(self):
        return self.title