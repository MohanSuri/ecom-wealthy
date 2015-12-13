from .models import *

from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
	class Meta(object):
		model= Product
		fields=(
			'product_name',
			'product_price',
			'product_description',
			'product_color',
			'sub_category',
			)

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
			'category_name',
			'sub_category_name'
			)
