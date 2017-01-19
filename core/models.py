from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Category(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)

    #def default_category(self):
        #new Category(code: "ROOT", name: "Root Category")

    def __str__(self):
        return self.name

class Address(models.Model):
    pass


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Facility(models.Model):
    pass

class Location(models.Model):
    pass

class InventoryItem(models.Model):
    lot_number = models.CharField(max_length=100, blank=True, null=True)
    expiration_date = models.DateField(null=True)



class AbstractProduct(models.Model):
    class Meta:
        abstract = True

    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey('auth.User')

    # Associations
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, related_name='products')

    def __str__(self):
        return self.name




class Product(AbstractProduct):
    pass

