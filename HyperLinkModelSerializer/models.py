from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField( max_length=50)
    roll_no=models.IntegerField()
    city=models.CharField(max_length=10)
    pass_by=models.CharField(max_length=10,default=0)
