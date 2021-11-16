from django.db import models

# Create your models here.

class Company(models.Model):
    CompanyId = models.AutoField(primary_key=True)
    companyname=models.CharField(max_length=25)
    location=models.CharField(max_length=25)
    Time=models.TimeField(auto_now_add=True,blank=False)
    DateOfJoining =models.DateField()
    Post=models.CharField(max_length=25)
    vacancy=models.IntegerField()
    
    # CompanyId = models.AutoField(primary_key=True)
    # CompanyName = models.CharField(max_length=500)
    # Department = models.CharField(max_length=500)
    # DateOfJoining = models.DateField()


