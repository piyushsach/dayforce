from django.db import models


class Register(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    
    


    def __str__(self):
        return self.name


class Feedback(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    suggestion=models.CharField(max_length=200)


  
    
    


    def __str__(self):
        return self.name





class Srs(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    suggestion=models.CharField(max_length=200)
    shift=models.CharField(max_length=50)
    meeting=models.CharField(max_length=50)
    overall=models.CharField(max_length=50)


  
    
    


    def __str__(self):
        return self.name


class Grs(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    types=models.CharField(max_length=50)
    detail=models.CharField(max_length=200)
    
    


  
    
    


    def __str__(self):
        return self.name











# Create your models here.
