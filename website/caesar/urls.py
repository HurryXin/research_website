# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views


app_name = 'caesar'
urlpatterns = [
    url(r'^', views.caesar, name='caesar'),
    url(r'^caesar', views.caesar, name='caesar'),
]
