from .models import *

from rest_framework import serializers
'''
Contains serializers for the models: Products, Users, Categories, SubCategories,Orders

'''
class ProductSerializer(serializers.ModelSerializer):
	class Meta(object):
		model= Product
		fields=(
			'product_name',
			'product_price',
			'product_description',
			'product_color',
			)

class UserSerializer(serializers.ModelSerializer):
	class Meta(object):
		model= Users
		fields=('user_id','user_name','password','user_mail_id','user_phone_number','user_address')

class OrderSerializer(serializers.ModelSerializer):
	class Meta(object):
		model= Orders
		fields=('order_id','user_id','order_address','payment_mode','product_name','product_price','product_description','order_phone_number')		


class CategorySerializer(serializers.ModelSerializer):
	class Meta(object):
		model= Categories
		fields=(
			'category_name',
			)

class SubCategorySerializer(serializers.ModelSerializer):
	class Meta(object):
		model= SubCategories
		fields=(
			'sub_category_name',
			)
