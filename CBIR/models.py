from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CBIRS_IMAGE(models.Model):
     id = models.BigIntegerField
     class_name = models.CharField(max_length=20, default='a')
     local = models.CharField(max_length=200, default='a')
     def __unicode__(self):
        return self.class_name

class CBIRS_1024_Feature(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    value = models.TextField(max_length=5000, default='a')


class CBIRS_64_Feature(models.Model):
     id = models.CharField(max_length=20, primary_key=True)
     value = models.CharField(max_length=200, default='a')
     tag = models.CharField(max_length=20, default='a', db_index=True)