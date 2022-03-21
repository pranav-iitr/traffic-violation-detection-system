from tokenize import Number
from django.db import models


class two_weeler(models.Model):
    name = models.CharField(max_length=500)
    file = models.FileField(upload_to='video')
    date_added = models.DateField(auto_now_add=True)


class fines(models.Model):
    name = models.CharField(max_length=50)
    fine = models.IntegerField()

class crime(models.Model):
    Number_Plate = models.TextField()
    proof = models.ImageField()
    
    

