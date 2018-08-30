# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models




# Create your models here.

class Churchguide(models.Model):
	service = models.CharField(max_length=100)
	service_date = models.DateTimeField('date of service')
	
class ServiceItem(models.Model):
	heading = models.CharField(max_length=100)
	content = models.CharField(max_length=100)
		
