from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class CreditCard(models.Model):
    name=models.CharField(max_length=40)
    expDate=models.DateField()
    type=models.CharField(max_length=12)
    friendlyName=models.CharField(max_length=15)
    cardNumber=models.CharField(max_length=22)
    user=models.ForeignKey(User)