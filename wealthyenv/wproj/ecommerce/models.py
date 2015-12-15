from __future__ import unicode_literals

from django.db import models

'''
Models for the fields: Products, Users, Categories, SubCategories,Orders
'''


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
    def __str__(self):              # __unicode__ on Python 2
        return "%s" % (self.product_name)


class Users(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=25,blank=False)
    password=models.CharField(max_length=25,blank=False) 
    user_mail_id=  models.EmailField()
    user_phone_number=models.IntegerField(default=0)
    user_address=models.CharField(max_length=300,default='')        	
    def __str__(self):              # __unicode__ on Python 2
        return "%s" % (self.user_name)

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(Users, on_delete=models.CASCADE)
    order_address=models.CharField(max_length=300,blank=False)
    payment_mode=models.CharField(max_length=20,blank=False)
    product_name=models.CharField(max_length=10,blank=False)
    product_price=models.IntegerField(blank=False)
    product_description=models.CharField(max_length=300)
    order_phone_number=models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
        return "%s" % (self.product_description)

  
        



# Create your models here.
