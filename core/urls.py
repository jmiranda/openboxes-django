#!python
# log/urls.py
from core.views import ProductSearchListView, ProductListView, ProductUpdateView, ProductDeleteView, ProductCreateView
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^products/$', ProductListView.as_view(), name='product-list-view'),
    url(r'^products/create/$', ProductCreateView.as_view(), name='product-create-view'),
    url(r'^products/(?P<product_id>[0-9]+)/$', views.product_details, name='product-details-view'),
    url(r'^products/(?P<product_id>[0-9]+)/edit/$', ProductUpdateView.as_view(), name='product-update-view'),
    url(r'^products/(?P<product_id>[0-9]+)/delete/$', ProductDeleteView.as_view(), name='product-delete-view'),
    url(r'^products/search/$', ProductSearchListView.as_view(), name='product-search-list-view'),
]
