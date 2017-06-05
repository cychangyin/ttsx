from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class TypeInfo(models.Model):
    title = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table='typeinfo'
    def __str__(self):
        return self.title.encode('utf-8')

class GoodsInfo(models.Model):
    title=models.CharField(max_length=100)
    tpic=models.ImageField(upload_to='goods')
    tprice=models.DecimalField(max_digits=5,decimal_places=2)
    isDelete=models.BooleanField(default=False)
    gunit=models.CharField(max_length=20,default='500 g')
    gclick=models.IntegerField(default=0)
    gjianjie=models.CharField(max_length=200)
    gkuncun=models.IntegerField(default=100)
    gcontent=HTMLField()
    gtype=models.ForeignKey(TypeInfo)
    def __str__(self):
        return self.title.encode('utf-8')