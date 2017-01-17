from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Product(models.Model):

    code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    description = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey('auth.User')
    category = models.ForeignKey('')


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Category(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)