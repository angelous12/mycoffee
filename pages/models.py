import imp
from django.db import models
from datetime import datetime
from django.utils.text import slugify
# Create your models here.

class Product(models.Model):
    new_old = [
        ('Old','Old'),
        ('New','New'),
    ]
    name = models.CharField(max_length=20)
    description = models.TextField()
    category = models.ForeignKey('Category' , on_delete=models.CASCADE,verbose_name='Choose category', null=True , blank=True)
    old_new = models.CharField(choices=new_old , verbose_name='Choose New & Old' , null=True , blank=True , max_length=10)
    price = models.DecimalField(max_digits=6 , decimal_places=0)
    old_price = models.DecimalField(max_digits=6 , decimal_places=0)
    slug = models.SlugField(blank=True , null=True)
    photo = models.ImageField(upload_to='photos/%y/%m/%d' , null=True , blank=True)
    date  = models.DateTimeField(default=datetime.now())
    active = models.BooleanField(default=True)
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Product,self).save(*args, **kwargs)
    def __str__(self):
        return self.name
    class Meta:
        ordering=['-date'] 

class Category(models.Model):
    name_category = models.CharField(max_length=50)
    def __str__(self):
        return self.name_category