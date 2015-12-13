from django.conf.urls import url

from . import views
from . import api
from rest_framework.urlpatterns import format_suffix_patterns

app_name='ecommerce'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/products$',api.ProductList.as_view(), name='products'),
    #url(r'^(?P<question_id>[0-9]+)/results/$',views.results, name='results'),
    url(r'^api/categories$', api.CategoryList.as_view(), name='categories'),
    url(r'^api/subcategories?$', api.SubCategoryList.as_view(), name='subcategories'),
    #url(r'^api/subcategories(?P<pk>[0-9]+)/$', api.SubCategoryList.as_view(), name='subcategories'),
    url(r'^api/products?$', api.ProductBySubCat.as_view(), name='productBySubCat'),
    #url(r'^api/subcategories?$', api.SubCategoryList.as_view(), name='subcategories'),
]