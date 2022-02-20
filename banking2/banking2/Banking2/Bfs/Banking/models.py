from django.db import models

# Create your models here.
class Register(models.Model):
    fullname=models.CharField(max_length=100,blank=False)
    username=models.CharField(max_length=100,blank=False,unique=True)
    email=models.EmailField(max_length=100,blank=False)
    mobileno=models.CharField(max_length=100,blank=False)
    password=models.CharField(max_length=100,blank=False)
    cpassword=models.CharField(max_length=100,blank=False)
    gender_choices=(('Male','Male'),('Female','Female'))
    gender=models.CharField(max_length=100,blank=False,choices=gender_choices)
    account_choices=(('Savings','Savings'),('Current','Current'),('Salary','Salary'))
    account=models.CharField(max_length=100,blank=False,choices=account_choices)
    class Meta:
        db_table = "userreg_table"