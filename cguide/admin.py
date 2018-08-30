# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Churchguide, ServiceItem


admin.site.register(Churchguide)
admin.site.register(ServiceItem)


# Register your models here.
