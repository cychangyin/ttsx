from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname=models.CharField(max_length=30)
    upasswd=models.CharField(max_length=40)
    uemail = models.CharField(max_length=50)
    ushou= models.CharField(max_length=30,default='')
    uaddrees=models.CharField(max_length=100,default='')
    upostalcode=models.CharField(max_length=8,default='')
    uphone=models.CharField(max_length=20,default='')
    class Meta:
        db_table='userinfo'

