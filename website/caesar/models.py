# -*- coding: utf-8 -*-

from django.db import models

class BrainModule(models.Model):
    trade_id = models.PositiveIntegerField(default=0)
    module = models.PositiveSmallIntegerField(default=0)
    predict = models.NullBooleanField()
    result = models.NullBooleanField()

class Quota(models.Model):
    accuracy = models.FloatField(default=0)
    precision = models.FloatField(default=0)
    recall = models.FloatField(default=0)
    disturb = models.FloatField(default=0)
