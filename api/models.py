from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
class PersonalInfo(models.Model):
    fullname=models.CharField(max_length=30,null=True)
    emailid = models.EmailField(max_length=255, null=False)
    date_of_birth=models.DateField(max_length=10)
    gender=models.CharField(max_length=25, null=False)
    #about has to be in form of Text Field
    about=models.TextField()

class UserSignUp(models.Model):
    username = models.CharField(max_length=25, null=True, blank=True)
    password=password=models.CharField(null=False,blank=False,max_length=10)
    confirm_password = models.CharField(null=False,blank=False,max_length=10) 

class SignUpOtp(models.Model):
    otp=models.IntegerField(null=False,blank=False)
