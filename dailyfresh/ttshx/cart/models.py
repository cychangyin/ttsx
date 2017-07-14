from django.db import models
from goods.models import *
from ttusers.models import *
# Create your models here.
class CartInfo(models.Model):
    goods=models.ForeignKey(GoodsInfo)
    count=models.IntegerField()
    user=models.ForeignKey(UserInfo)
    class Meta:
        db_table='cartinfo'