from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from health_care_app.models import Patients


def frontend(request):
    return render(request, 'frontend.html')


@login_required(login_url='login')
def backend(request):
    return render(request, 'backend.html')


@login_required(login_url='login')
def add_patient(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('age') and request.POST.get('gender') or request.POST.get('note'):  # noqa
            patient = Patients()
            patient.name = request.POST.get('name')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.note = request.POST.get('note')
            patient.save()
            messages.success(request, 'Patient added sucessfully!')
            return HttpResponseRedirect('/backend')
    else:
        return render(request, 'add.html')
