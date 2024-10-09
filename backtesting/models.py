from django.db import models
import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Condition(models.Model):
    formel = models.CharField(max_length=200)

class Tradable(models.Model):
    name = models.CharField(max_length=500)
    type = models.CharField(max_length=500)

class Price(models.Model):
    tradable = models.ForeignKey(Tradable, default=1, null=True, on_delete=models.SET_NULL)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volumne_currency = models.FloatField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)


class Strategy(models.Model):
    margin = models.FloatField()
    takeProfit = models.FloatField()
    stopLoss = models.FloatField()


