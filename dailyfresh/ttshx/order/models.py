from django.db import models

# Create your models here.
class OrderInfo(models.Model):
    user=models.ForeignKey('ttusers.UserInfo')
    odate=models.DateTimeField(auto_now_add=True)
    oIsPay=models.BooleanField(default=False)
    ototal=models.DecimalField(max_digits=6,decimal_places=2)
    oaddress=models.CharField(max_length=150)

class OrderDetailInfo(models.Model):
    goods=models.ForeignKey('goods.GoodsInfo')
    order=models.ForeignKey(OrderInfo)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    count=models.IntegerField()