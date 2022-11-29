from django.db import models

# Create your models here.


class Studentprofile(models.Model):
    first_name = models.CharField(max_length= 50, null= False)
    middle_name = models.CharField(max_length= 50, null= False)
    last_name = models.CharField(max_length= 50, null= False)
    date_of_birth = models.DateField(max_length=11, null=False)
    age = models.IntegerField(null=False)
    course = models.CharField(max_length=250, null=False)
    address = models.CharField(max_length=250, null=False)
    
    