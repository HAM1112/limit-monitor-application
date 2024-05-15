from celery import shared_task
from datetime import datetime
from monitor.models import Criterion
from django.core.mail import EmailMessage ,send_mail

from django.conf import settings
import requests

@shared_task
def daily_status_update():
    city = 'London'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={settings.API_KEY}'
    city_weather = requests.get(url).json()
    
    records = Criterion.objects.filter(frequency='day')
    for record in records:
        para = record.parameter
        if record.status == "Pending" and  eval(f"{record.threshold} {record.operator} {city_weather['main'][para]} "):
            message = f"Criteria has Completed"
            subject = 'Criteria status'
            from_email = settings.EMAIL_HOST_USER
            to_email = [record.user.email]
            send_mail(subject,message,from_email , to_email)
            record.status = 'Completed'
            record.save()
    print('daily')
    
@shared_task
def monthly_status_update():
    city = 'London'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={settings.API_KEY}'
    city_weather = requests.get(url).json()
    
    records = Criterion.objects.filter(frequency='month')
    for record in records:
        para = record.parameter
        if record.status == "Pending" and  eval(f"{record.threshold} {record.operator} {city_weather['main'][para]} "):
            message = f"Criteria has Completed"
            subject = 'Criteria status'
            from_email = settings.EMAIL_HOST_USER
            to_email = [record.user.email]
            send_mail(subject,message,from_email , to_email)
            record.status = 'Completed'
            record.save()
    print('montly')
    
    
@shared_task
def yearly_status_update():
    city = 'London'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={settings.API_KEY}'
    city_weather = requests.get(url).json()
    
    records = Criterion.objects.filter(frequency='year')
    for record in records:
        para = record.parameter
        if record.status == "Pending" and  eval(f"{record.threshold} {record.operator} {city_weather['main'][para]} "):
            message = f"Criteria has Completed"
            subject = 'Criteria status'
            from_email = settings.EMAIL_HOST_USER
            to_email = [record.user.email]
            send_mail(subject,message,from_email , to_email)
            record.status = 'Completed'
            record.save()
    print('yearly')
    