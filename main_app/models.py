from django.db import models
from datetime import date

# Create your models here.
class Budget(models.Model):
    month = models.CharField(max_length=100, default="0")
    date = models.DateField('Date')
    income = models.IntegerField(default=0)
    car = models.IntegerField(default=0)
    
    

