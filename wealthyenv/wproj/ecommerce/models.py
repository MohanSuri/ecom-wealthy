from __future__ import unicode_literals

from django.db import models




class Categories(models.Model):
    category_id= models.AutoField(primary_key=True)
    category_name= models.CharField(max_length=25,default="")
    def __str__(self):              # __unicode__ on Python 2
        return self.category_name

class SubCategories(models.Model):
    sub_category_id = models.AutoField(primary_key=True)
    category_id= models.ForeignKey(Categories, on_delete=models.CASCADE)
    sub_category_name= models.CharField(max_length=25,default="")
    def __str__(self):              # __unicode__ on Python 2
        return "%s" % (self.sub_category_name)    

class Product(models.Model):
    #This class represents product details
    product_id=models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=25,default="")
    product_price=models.DecimalField(max_digits=9,decimal_places=6,default=0)
    product_description=models.CharField(max_length=1000,default="")
    product_color=models.CharField(max_length=10,default="")
    sub_category_id = models.ForeignKey(SubCategories, on_delete=models.CASCADE)

            	




# Create your models here.
