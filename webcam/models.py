from tokenize import Number
from django.db import models


class two_weeler(models.Model):
    name = models.CharField(max_length=500)
    file = models.FileField(upload_to='video')
    date_added = models.DateField(auto_now_add=True)



class crime(models.Model):
    name = models.TextField()
    proof = models.ImageField()
    
    

