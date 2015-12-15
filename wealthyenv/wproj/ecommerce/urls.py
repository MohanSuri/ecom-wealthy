from django.conf.urls import url

from . import views
from . import api
from rest_framework.urlpatterns import format_suffix_patterns

app_name='ecommerce'
'''
Url patterns for allowing rest calls
'''
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/products$',api.ProductList.as_view(), name='products'),
    url(r'^api/categories$', api.CategoryList.as_view(), name='categories'),
    url(r'^api/subcategories/(?P<category_id>[0-9]+)/$', api.SubCategory.as_view(), name='subcategories'),
    url(r'^api/products/(?P<sub_category_id>[0-9]+)/$', api.ProductBySubCat.as_view(), name='productBySubCat'),
    url(r'^api/products/(?P<product_name>[a-zA-Z\s0-9]+)/$', api.ProductByName.as_view(), name='productByName'),
    url(r'^api/orders/(?P<user_id>[a-zA-Z\s0-9]+)/$', api.MyOrders.as_view(), name='ordersByUsers'),
	url(r'^api/user/new/$', api.createUser, name='newuser'), 
	url(r'^api/orders/new/$', api.Order, name='newOrder'),     
]