from .models import Product, Categories
from serializer import *
from django.core import serializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import json

class  ProductList(APIView):
	def get(self, request, format=json):
		products=Product.objects.all()
		serialized_products=ProductSerializer(products, many=True)
		#serialized_products = serializers.serialize("json", products)
		#return HttpResponse(data, mimetype="application/json")
		return Response(serialized_products.data)


class CategoryList(APIView):
	"""docstring for ClassName"""
	def get(self, request, format=json):
		categories=Categories.objects.all()
		serialized_categories=CategorySerializer(categories, many=True)
		return Response(serialized_categories.data)
		

class SubCategoryList(APIView):
	"""docstring for ClassName"""
	def get(self, request, format=json):
		sub_categories=SubCategories.objects.all()
		serialized_sub_categories=SubCategorySerializer(sub_categories, many=True)
		return Response(serialized_sub_categories.data)

class SubCategory(APIView):
	def getObj(self, Category):
		try:
			return SubCategories.objects.filter(Categories__category_name=Category)
			
		except Exception, e:
			raise Http404
		else:
			pass
		finally:
			pass

	def get(APIView, request, Category, format=json):
		Category = request.GET.get('Category')
		sub_cat=self.getObj(Category)
		serialized_sub_categories=SubCategorySerializer(sub_cat)
		return Response(serialized_sub_categories.data)


class ProductBySubCat(APIView):
	def getObj(self, sub_cat):
		try:
			return Product.objects.filter(SubCategories__sub_category_name=sub_cat)
			
		except Exception, e:
			raise Http404
		else:
			pass
		finally:
			pass

	def get(APIView, request, Category, format=json):
		sub_cat = request.GET.get('SubCategory')
		product=self.getObj(sub_cat)
		serialized_products=ProductSerializer(product)
		return Response(serialized_products.data)



