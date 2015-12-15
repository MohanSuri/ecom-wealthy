from .models import Product, Categories
from serializer import *
from django.core import serializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
import json


class  ProductList(APIView):
	#Gets List of all products 
	def get(self, request, format=json):
		products=Product.objects.all()
		serialized_products=ProductSerializer(products, many=True)
		return Response(serialized_products.data)


class CategoryList(APIView):
	#Gets list of all categories
	def get(self, request, format=json):
		categories=Categories.objects.all()
		serialized_categories=CategorySerializer(categories, many=True)
		return Response(serialized_categories.data)

class SubCategory(APIView):
	#Lists the subcategories based on Category name
	def getObj(self, category_id):
		try:
			return SubCategories.objects.filter(category_id=category_id)
			
		except Exception, e:
			raise Http404
		else:
			pass
		finally:
			pass

	def get(self, request, category_id, format=json):
		sub_cat=self.getObj(category_id)
		serialized_sub_categories=SubCategorySerializer(sub_cat, many=True)
		return Response(serialized_sub_categories.data)


class ProductBySubCat(APIView):
	#Lists Products based on Subcategory name
	def getObj(self, sub_category_id):
		try:
			return Product.objects.filter(sub_category_id=sub_category_id)
			
		except Exception, e:
			raise Http404
		else:
			pass
		finally:
			pass

	def get(self, request, sub_category_id, format=json):
		product=self.getObj(sub_category_id)
		serialized_products=ProductSerializer(product, many=True)
		return Response(serialized_products.data)

class ProductByName(APIView):
	#Get product by it's full name
	def getObj(self, product_name):
		try:
			return Product.objects.filter(product_name=product_name)
			
		except Exception, e:
			raise Http404
		else:
			pass
		finally:
			pass

	def get(self, request, product_name, format=json):
		product=self.getObj(product_name)
		serialized_products=ProductSerializer(product, many=True)
		return Response(serialized_products.data)

@api_view(['POST'])
def createUser(request):
	#Create a new User profile
	if request.method=='POST':
		data = request.body
		serializer = UserSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
        	return Response(serializer.data, status=status.HTTP_201_CREATED)
    	else:
        	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def Order(request):
	#Post an order
	if request.method=='POST':
		data = request.body
		serializer = OrderSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
        	return Response(serializer.data, status=status.HTTP_201_CREATED)
    	else:
        	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyOrders(APIView):
	#Get all orders for a given user id
	def getObj(self, user_id):
		try:
			return Product.objects.filter(user_id=user_id)
			
		except Exception, e:
			raise Http404
		else:
			pass
		finally:
			pass

	def get(self, request, user_id, format=json):
		order=self.getObj(user_id)
		serialized_products=ProductSerializer(order, many=True)
		return Response(serialized_products.data)


