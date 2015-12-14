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
	def getObj(self, sub_category_id):
		try:
			print("-------------product---------------"+sub_category_id)
			return Product.objects.filter(sub_category_id=sub_category_id)
			
		except Exception, e:
			raise Http404
		else:
			pass
		finally:
			pass

	def get(self, request, sub_category_id, format=json):
		print("sub_categorie_id------------"+sub_category_id)
		product=self.getObj(sub_category_id)
		serialized_products=ProductSerializer(product, many=True)
		return Response(serialized_products.data)

class ProductByName(APIView):
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
		print("sub_categorie_id------------"+product_name)
		product=self.getObj(product_name)
		serialized_products=ProductSerializer(product, many=True)
		return Response(serialized_products.data)

@api_view(['POST'])
def createUser(request):
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
	if request.method=='POST':
		data = request.body
		serializer = OrderSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
        	return Response(serializer.data, status=status.HTTP_201_CREATED)
    	else:
        	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyOrders(APIView):
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


