from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Patient
from pprint import pprint

# Create your views here.


def home(request):

    if request.user.is_authenticated:
        groups = [group.name for group in request.user.groups.all()]
        print(groups)
        if 'H' in groups:
            patients = Patient.objects.all()
            return render(request, 'index.html', {'patients': patients})
        if 'R' in groups:
            patients = Patient.objects.all().exclude(first_name=None, last_name=None)
            return render(request, 'index.html', {'patients': patients})
        return render(request, 'index.html', {'error': 'You are not authorized to view this page'})
    return redirect("login")


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})
    if request.user.is_authenticated:
        return redirect("home")
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect("login")
