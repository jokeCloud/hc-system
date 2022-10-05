from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def frontend(request):
    return render(request, 'frontend.html')


@login_required(login_url='login')
def backend(request):
    return render(request, 'backend.html')


@login_required(login_url='login')
def add_patient(request):
    return render(request, 'add.html')
