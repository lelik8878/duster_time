from django.shortcuts import render

from datetime import datetime, timezone, timedelta
from .forms import DusterTimeForm
from .models import DusterTime

def get_home_page(request):
    context = {}
    return render(request, 'home_page.html', context)

def check_time(request):
    dusters = DusterTime.objects.all()
    current_duster = dusters.first()
    deadline = current_duster.duster_time
    deadline = deadline.replace(tzinfo=timezone.utc)
    time_remaining = deadline - datetime.now(timezone.utc) - timedelta(hours=3)
    if time_remaining > timedelta(0):
        duster = True
    else:
        duster = False
    days = time_remaining.days
    hours, remainder = divmod(time_remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    context = {'duster': duster, 'days': days, 'hours': hours, 'minutes': minutes}
    return render(request, 'check_time.html', context)

def set_time(request):
    dusters = DusterTime.objects.all()
    current_duster = dusters.first()
    form = DusterTimeForm()
    if request.method == 'POST':
        new_duster = DusterTimeForm(request.POST)
        if new_duster.is_valid():
            current_duster.duster_time = new_duster.cleaned_data['duster_time']
            current_duster.save()
    context = {'current_duster': current_duster, 'form': form}
    return render(request, 'set_time.html', context)
