
from django.db import models
from django.contrib.auth.models import User

class Criterion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parameter = models.CharField(max_length=50 ,  choices=[('temp', 'Temperature'), ('pressure', 'Pressure'), ('humidity', 'Humidity')])
    operator = models.CharField(max_length=50 ,  choices=[('>', 'Greater Than'), ('<', 'Lesser Than'), ('==', 'Equal To') , ('>=', 'Greater or Equal To'), ('<=', 'Lesser or Equal To')])
    threshold = models.FloatField()
    frequency = models.CharField(max_length=10, choices=[('day', 'Daily'), ('month', 'Monthly'), ('year', 'Yearly')])
    status = models.CharField(max_length=20, default='Pending')
    
    

