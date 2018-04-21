# -*- coding: utf-8 -*-

from django.db import models

class BrainModule(models.Model):
    trade_id = models.PositiveIntegerField(default=0)
    module = models.PositiveSmallIntegerField(default=0)
    predict = models.NullBooleanField()
    result = models.NullBooleanField()
    
