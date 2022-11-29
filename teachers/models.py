from django.db import models

# Create your models here.

class Teacherprofile(models.Model):
    first_name = models.CharField(max_length= 200, null=False)
    middle_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    username = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=50, null=False)
    address = models.CharField(max_length=50, null=False)
    subjects_handled = models.CharField(max_length=200, null=False)
    classes_handled = models.CharField(max_length=200, null=False)
    