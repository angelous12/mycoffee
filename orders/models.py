from pyexpat import model
from re import T
from django.db import models
from django.contrib.auth.models import User
from pages.models import Product
from datetime  import datetime
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    details = models.ManyToManyField(Product,through='OrderDetails')
    is_finished = models.BooleanField()
    def __str__(self):
        return  'User: ' + self.user.username + ', order id: ' +str(self.id)


class OrderDetails(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    order   = models.ForeignKey(Order , on_delete=models.CASCADE)
    price   = models.DecimalField(max_digits=6 , decimal_places=0)
    quantity = models.IntegerField()
    def __str__(self):
        return 'user: ' + self.order.user.username  + ' Name : ' + self.product.name + ' order id : ' + str(self.id)

    class Meta:
        ordering = ['-id']


class Coupon(models.Model):
    name = models.CharField(max_length=100 , blank=True , null=True)
    coupon = models.CharField(max_length=10)
    price  = models.DecimalField(max_digits=6 , decimal_places=0, blank=True , null=True)
    is_active = models.BooleanField(default=True)
    


    def __str__(self):
        return self.coupon