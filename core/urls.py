#!python
# log/urls.py
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^products/$', views.product_list, name='product_list'),
    url(r'^products/create/$', views.product_create.as_view(), name='product_create'),
    url(r'^products/(?P<product_id>[0-9]+)/$', views.product_details, name='product_details'),
    url(r'^products/(?P<product_id>[0-9]+)/edit/$', views.product_edit.as_view(), name='product_edit'),
    url(r'^products/(?P<product_id>[0-9]+)/delete/$', views.product_delete.as_view(), name='product_delete'),

]
