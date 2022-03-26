import os
from django.db import models
from django.core.files.base import ContentFile
from PIL import Image
from io import StringIO
from numpy import empty

from sympy import true

class two_weeler(models.Model):
    name = models.CharField(max_length=500)
    file = models.FileField(upload_to='video')
    date_added = models.DateField(auto_now_add=True)



class crime(models.Model):
    name = models.TextField()
    np= models.TextField(null=True,blank=True)
    proof = models.ImageField(upload_to="img")
    
class crime2(models.Model):
    name = models.TextField()
    np= models.TextField(null=True,blank=True)
    proof = models.ImageField(upload_to="img")
    

