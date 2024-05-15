from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage ,send_mail

from django.conf import settings
from .forms import CriterionForm 
from .models import Criterion 

# Create your views here.
import requests

@login_required(login_url='/account')
def home(request):
    criteria = Criterion.objects.filter(user=request.user)
    print(criteria)
    return render(request, 'monitor/criterion_list.html', {'criteria': criteria})


@login_required(login_url='/account')
def test(request):
    city = 'London'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={settings.API_KEY}'
    city_weather = requests.get(url).json()
    
    records = Criterion.objects.filter(frequency='day')
    for record in records:
        para = record.parameter
        if eval(f"{record.threshold} {record.operator} {city_weather['main'][para]} "):
            print('true')
            message = f"Criteria has Completed"
            subject = 'Criteria status'
            from_email = settings.EMAIL_HOST_USER
            to_email = [record.user.email]
            send_mail(subject,message,from_email , to_email)
     
    return 


@login_required(login_url='/account')
def criterion_create(request):
    if request.method == 'POST':
        form = CriterionForm(request.POST)
        if form.is_valid():
            criterion = form.save(commit=False)
            criterion.user = request.user
            criterion.save()
            return redirect('home')
    else:
        form = CriterionForm()
    return render(request, 'monitor/criterion_form.html', {'form': form})


@login_required(login_url='/account')
def criterion_update(request, pk):
    criterion = get_object_or_404(Criterion, pk=pk)
    if request.method == 'POST':
        form = CriterionForm(request.POST, instance=criterion)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CriterionForm(instance=criterion)
    return render(request, 'monitor/criterion_form.html', {'form': form})


@login_required(login_url='/account')
def criterion_delete(request, pk):
    criterion = get_object_or_404(Criterion, pk=pk)
    if request.method == 'POST':
        criterion.delete()
        return redirect('home')
    return render(request, 'monitor/criterion_confirm_delete.html', {'criterion': criterion})


