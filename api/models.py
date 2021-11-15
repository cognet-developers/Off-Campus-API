from django.db import models

class offcampus(models.Model):
    companyname=models.CharField(max_length=25,unique=True)
    location=models.CharField(max_length=25)
    Time=models.TimeField(auto_now_add=True,null=False,blank=False)
    Date=models.DateField()
    Post=models.CharField(max_length=25)
    vacancy=models.IntegerField()
    Package=models.BigIntegerField()

    def __str__(self):
        return self.companyname

